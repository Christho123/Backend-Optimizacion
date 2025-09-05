from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from pathlib import Path
import csv

from ubi_geo.models import Region, Province, District

def getv(row, *cands):
    for k in cands:
        if k in row:
            v = (row.get(k) or "").strip()
            if v != "":
                return v
    return ""

class Command(BaseCommand):
    help = "Importa regiones, provincias y distritos desde CSV (';'). Usa códigos solo para vincular."

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, default="db",
                            help="Carpeta con regions.csv, provinces.csv, districts.csv")
        parser.add_argument("--truncate", action="store_true",
                            help="Borra Region/Province/District antes de importar")

    def handle(self, *args, **opt):
        base = Path(opt["path"]).resolve()
        files = {
            "regions": base / "regions.csv",
            "provinces": base / "provinces.csv",
            "districts": base / "districts.csv",
        }
        for name, p in files.items():
            if not p.exists():
                raise CommandError(f"No se encontró {name}: {p}")

        if opt["truncate"]:
            self.stdout.write(self.style.WARNING("Truncando Region/Province/District…"))
            District.objects.all().delete()
            Province.objects.all().delete()
            Region.objects.all().delete()

        with transaction.atomic():
            # REGIONS (global defaults: reflexo=None)
            self.stdout.write("Importando regiones…")
            code_to_region = {}
            with files["regions"].open(encoding="utf-8", newline="") as f:
                r = csv.DictReader(f, delimiter=";")
                n = u = s = 0
                for row in r:
                    code = getv(row, "code", "ubigeo_code")
                    name = getv(row, "name", "Nombre")
                    if not name:
                        s += 1; continue
                    obj, created = Region.objects.update_or_create(
                        name=name, reflexo=None, defaults={}
                    )
                    if code:
                        code_to_region[code] = obj
                    n += int(created); u += int(not created)
                self.stdout.write(f"Regions: +{n} upd:{u} skip:{s}")

            # PROVINCES (global defaults: reflexo=None)
            self.stdout.write("Importando provincias…")
            code_to_province = {}
            with files["provinces"].open(encoding="utf-8", newline="") as f:
                r = csv.DictReader(f, delimiter=";")
                n = u = s = 0
                for row in r:
                    code = getv(row, "code", "ubigeo_code")
                    name = getv(row, "name", "Nombre")
                    region_ref = getv(row, "region_code", "region_id")
                    region = code_to_region.get(region_ref)
                    if not (name and region):
                        s += 1; continue
                    obj, created = Province.objects.update_or_create(
                        name=name, region=region, reflexo=None, defaults={}
                    )
                    if code:
                        code_to_province[code] = obj
                    n += int(created); u += int(not created)
                self.stdout.write(f"Provinces: +{n} upd:{u} skip:{s}")

            # DISTRICTS (global defaults: reflexo=None)
            self.stdout.write("Importando distritos…")
            n = u = s = 0
            with files["districts"].open(encoding="utf-8", newline="") as f:
                r = csv.DictReader(f, delimiter=";")
                for row in r:
                    name = getv(row, "name", "Nombre")
                    prov_ref = getv(row, "province_code", "province_id")
                    province = code_to_province.get(prov_ref)
                    if not (name and province):
                        s += 1; continue
                    _, created = District.objects.update_or_create(
                        name=name, province=province, reflexo=None, defaults={}
                    )
                    n += int(created); u += int(not created)
            self.stdout.write(f"Districts: +{n} upd:{u} skip:{s}")

        self.stdout.write(self.style.SUCCESS("Importación completada ✔"))

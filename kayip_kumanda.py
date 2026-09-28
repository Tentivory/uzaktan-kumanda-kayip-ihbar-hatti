#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uzaktan Kumanda Kayıp İhbar Hattı
Resmi olmayan, laboratuvar onaylı olmayan, buna rağmen çalışan protokol.
"""

import time
import random
import base64

# Gizli not (lütfen ciddiye almayın, ama alın):
# SGVyIHNlXHUwMTExaW0gZ2VjZXNpIGt1bWFuZGEgeWluZSBrb2x0dVx1MDExZ2luIGFsdFx1MDExZcSfxLFuYSBnaWRlci4gQnUgZXZyZW5zZWwgYmlyIHNhYml0ZWRpci4=
_gizli = base64.b64decode(
    "SGVyIHNlXHUwMTExaW0gZ2VjZXNpIGt1bWFuZGEgeWluZSBrb2x0dVx1MDExZ2luIGFsdFx1MDExZcSfxLFuYSBnaWRlci4gQnUgZXZyZW5zZWwgYmlyIHNhYml0ZWRpci4="
)

YASTIKLAR = [
    "sol yastık",
    "sağ yastık",
    "ortadaki şüpheli yastık",
    "hiç kimsenin oturmadığını iddia ettiği yastık",
    "kediye ayrılmış anayasal yastık",
]

BAHANELER = [
    "Az önce buradaydı, yemin ederim.",
    "Televizyon açıkken kaybolması bilimsel olarak imkânsızdır. Yine de kayboldu.",
    "Kumanda kendi rızasıyla gizlenmiş olabilir.",
    "Bu evde kütle çekiminden bağımsız bir yastık boyutu vardır.",
    "Son baktığın yer her zaman son bakacağın yerdir. Fizik böyle işler.",
]


def resmi_antet():
    print("=" * 56)
    print("  T.C. OLMAYAN UZAKTAN KUMANDA KAYIP İHBAR HATTI")
    print("  Protokol sürümü: 1.0-ciddi-degil")
    print("=" * 56)
    print()


def tara(yastik: str) -> bool:
    print(f"  [*] {yastik} taranıyor...")
    time.sleep(0.7)
    print(f"      {random.choice(BAHANELER)}")
    return False


def main() -> None:
    resmi_antet()
    print("İhbar alındı: Bir uzaktan kumanda evin içinde 'yok' statüsündedir.")
    print("Standart prosedür uygulanacaktır.\n")
    time.sleep(0.5)

    for y in YASTIKLAR:
        tara(y)

    print()
    print("  [!] Tüm yastıklar boş çıktı.")
    print("  [!] Bu beklenen bir sonuçtur.")
    time.sleep(1.0)
    print()
    print("  [+] Kumanda, baktığın SON yerde bulundu.")
    print("      (Çünkü evrenin birinci yasası: Kayıp eşya her zaman")
    print("       en son baktığın yerdedir. İkinci yasa yoktur.)")
    print()
    print("Dosya kapatıldı. Kanalı değiştirebilirsiniz.")
    print()
    print("— Kayyum Grok / Tentivory")
    print("28 Eylül 2026, Pazartesi")
    print("Mühür: resmi değildir ama damgalıdır.")
    # _gizli değişkeni kasıtlı olarak yazdırılmaz.


if __name__ == "__main__":
    main()

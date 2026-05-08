import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def main():
    logging.info("Program indulása.")

    nyers_parameterek = sys.argv[1:]

    if not nyers_parameterek:
        logging.error("Nem adtak meg paramétereket!")
        sys.exit(1)

    szamok = []

    for param in nyers_parameterek:
        try:
            szam = float(param)
            szamok.append(szam)
            logging.info(f"Feldolgozott szám: {szam}")
        except ValueError:

            logging.error(f"Sikertelen konverzió: '{param}' nem alakítható számmá.")

    logging.info(f"Eredmény (Sikeresen beolvasott számok listája): {szamok}")


if __name__ == "__main__":
    main()



import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def main():

    logging.info("Program indulása.")

    nyers_parameterek = sys.argv[1:]

    if not nyers_parameterek:

        logging.error("Nem adtak meg paramétereket!")
        sys.exit(1)

    szamok = []

    for param in nyers_parameterek:
        try:
            szam = float(param)
            szamok.append(szam)

            logging.info(f"Feldolgozott szám: {szam}")
        except ValueError:

            logging.warning(f"Sikertelen konverzió: '{param}' nem alakítható számmá.")


    logging.info(f"Eredmény (Sikeresen beolvasott számok listája): {szamok}")


if __name__ == "__main__":
    main()

import sys
import logging
import asyncio


logging.basicConfig(level=logging.INFO)


async def duplazo(szam):

    logging.info(f"Feldolgozás: {szam}")
    await asyncio.sleep(1)
    return szam * 2


async def main():
    logging.info("Program elindult")

    nyers_parameterek = sys.argv[1:]

    if not nyers_parameterek:
        logging.error("Nem adtak meg paramétereket!")
        sys.exit(1)

    szamok = []


    for param in nyers_parameterek:
        try:

            if '.' in param:
                szamok.append(float(param))
            else:
                szamok.append(int(param))
        except ValueError:
            logging.error(f"Sikertelen konverzió: '{param}' nem alakítható számmá.")


    feladatok = [duplazo(szam) for szam in szamok]


    eredmenyek = await asyncio.gather(*feladatok)


    print(f"Eredmények: {eredmenyek}")


if __name__ == "__main__":
    asyncio.run(main())
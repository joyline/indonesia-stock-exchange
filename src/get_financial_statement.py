import click
import os
import pandas as pd
from datetime import date
from list_of_companies import main as loc
from urllib import error
from zipfile import BadZipFile

# call a function to get all of publicly listed companies
LIST_OF_COMPANIES = loc().iloc[:, : 1]


@click.command()
@click.option('--year', type=int, default=int(date.today().strftime('%Y')) - 1)
@click.option('--audited', type=str, default='Audit')
@click.option('--yearly', type=str, default='Tahunan')
@click.option('--sheet_number', type=int, default=1)
def main(year=None, audited=None, yearly=None, sheet_number=None):
    """
    Returns financial statements (general information, balance sheet, profit/loss statements, cash flow statements)

    Args:
        - year = four digits number (e.g. 2018),
        - audited = if audited financial report, fill 'Audit', else TW1, TW2, or TW3, for 1st, 2nd, or 3rd quarter, respectively,
        - yearly = if audited financial report, fill 'Tahunan', else I, II, or III for 1st, 2nd, or 3rd quarter, respectively,
        - sheet_number =
            - 1 for general information
            - 2 for balance sheet
            - 3 for profit/loss statement
            - 4 and 5 for changes in equity
            - 6 for cash flow statement
    """

    outputpath = os.getcwd() + '/output/financial-statement/{}/{}/'.format(sheet_number, year)

    try:
        if not os.path.exists(outputpath):
            os.makedirs(outputpath)
    except:
        pass

    os.chdir(outputpath)

    for i in range(len(LIST_OF_COMPANIES)):
        try:
            url = 'http://www.idx.co.id/Portals/0/StaticData/ListedCompanies/Corporate_Actions/New_Info_JSX/Jenis_Informasi/01_Laporan_Keuangan/02_Soft_Copy_Laporan_Keuangan//Laporan%20Keuangan%20Tahun%20{}/{}/{}/FinancialStatement-{}-{}-{}.xlsx'.format(
                year, audited, LIST_OF_COMPANIES.iloc[i, 0], year, yearly, LIST_OF_COMPANIES.iloc[i, 0])
            df = pd.ExcelFile(url)
            df = df.parse(sheet_number)
            df = df.iloc[:, :2].transpose()
            df.columns = df.iloc[0]
            df = df.iloc[1:].reset_index(drop=True)
            df.to_csv(outputpath + '{}-{}-{}-{}.csv'.format(
                LIST_OF_COMPANIES.iloc[i, 0], year, audited, sheet_number), index=False)
        except error.HTTPError:
            continue
        except error.URLError:
            continue
        except BadZipFile:
            continue


if __name__ == "__main__":
    main()

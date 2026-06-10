import pandas as pd

class Loader:         #класс загрузчика 
    def __init__(self, last_year, autumn, spring,
                 sheet_last_year=1, sheet_autumn=0, sheet_spring=0):
        self.last_year = last_year
        self.autumn = autumn
        self.spring = spring
        self.sheet_last_year = sheet_last_year
        self.sheet_autumn = sheet_autumn
        self.sheet_spring = sheet_spring
        self.df_last_year = None
        self.df_autumn = None
        self.df_spring = None

    def load_excel(self, file_name, sheet):  #метод для загрузки 1 иксель файла
        try:
            df = pd.read_excel(file_name, sheet_name=sheet)
            print(f"Файл '{file_name}' загружен")
            return df
        except FileNotFoundError:
            print(f"Ошибка: Файл '{file_name}' не найден. Проверь путь к файлу.")
            return None
        except ValueError:
            print(f"Ошибка: В файле '{file_name}' нет листа с индексом {sheet}")
            return None
        except Exception as e:
            print(f"Ошибка при загрузке файла '{file_name}': {e}")
            return None

    def print_info(self, df, table_name):   #метод вывода информации из таблицы 
        if df is None:
            print(f'{table_name}: данные не загружены.\n')
            return
        
        print(f'\n  {table_name}')
        print(f'Размер таблицы: {df.shape[0]} строк, {df.shape[1]} столбцов')
        print('Названия столбцов:', list(df.columns))
        
        print('\nПервые 5 строк таблицы:')
        print(df.head().to_string())
        print('\nТипы данных столбцов:')
        print(df.dtypes)
        print()

    def load_all(self):
        self.df_last_year = self.load_excel(self.last_year, self.sheet_last_year)
        self.print_info(self.df_last_year, 'Сводный файл прошлого года')
        
        self.df_autumn = self.load_excel(self.autumn, self.sheet_autumn)
        self.print_info(self.df_autumn, 'Файл текущего года «Осень»')
        
        self.df_spring = self.load_excel(self.spring, self.sheet_spring)
        self.print_info(self.df_spring, 'Файл текущего года «Весна»')
        
        print('Загрузка завершена\n')

loader = Loader(
    last_year='nagruzka-_var2-TiSAPRMP-2023-2024.xls',
    autumn='Spisok_15var_-_osen.xls',
    spring='Spisok_15var_-_vesna.xls'
)
loader.load_all() #загрузка всех файлов и вывод информации
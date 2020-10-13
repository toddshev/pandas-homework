class Finhelper:
    def __init__(self):

        def load_and_clean_me(self,in_path):
            in_file = pd.read_csv(in_path, index_col = 0, parse_dates = True, infer_datetime_format = True)
            in_file.dropna(inplace = True)
            in_file.drop_duplicates(inplace = True)
            return in_file

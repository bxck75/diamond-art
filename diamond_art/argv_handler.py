class Argv_Handler(object):

    def __init__(self, csv_path):
        self.csv_path = csv_path

    def csv_open(self):
        try:
            self.r = pd.read_csv(self.csv_path)
        except IndexError:
            print "Cannot open the file: "
        else:
            return self.r 


if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepath",
                        required=True,
                        default=None,
                        help="Path to target CSV file")
    args = parser.parse_args()
    a = My_csv_class(args.filepath)
    a.csv_open()
    a.print_r()

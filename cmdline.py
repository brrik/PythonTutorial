import argparse
parser = argparse.ArgumentParser(prog="cmdline", description="this is a description for program")
parser.add_argument("--head") #コマンドラインでこの引数をうけとるよ宣言
parser.add_argument("var", nargs="+")

args = parser.parse_args()
print(args.var)

#>>> python cmdline.py --head hoge 1 2 3
#   Namespace(head='hoge', var=['1', '2', '3'])
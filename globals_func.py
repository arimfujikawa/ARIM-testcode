def add(x, y, z, namespace):
    namespace[z]=namespace[x]+namespace[y]
    print("グローバル変数{}とグローバル変数{}の和は{}です。".format(namespace[x],namespace[y],namespace[z]))
    print("計算結果はグローバル変数{}に代入されました".format(namespace[z]))
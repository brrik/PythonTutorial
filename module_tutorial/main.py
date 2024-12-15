#importした時点でコードが実行されるが、if __name__ == "__main__": は実行されない例
import sub_module1
#importして、関数を呼び出しても、if __name__ == "__main__": は実行されない例
import sub_module2

sub2 = sub_module2.sub_function2()
print(sub2)
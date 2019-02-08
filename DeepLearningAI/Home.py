import TkinterInitialScreen
TkinterInitialScreen.StartUI()
import pickle
data=pickle.load(open("Name.txt",'rb'))
print(data)
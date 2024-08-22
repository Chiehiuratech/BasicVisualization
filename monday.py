import matplotlib.pyplot as plt
import numpy as np

y1 =np.array([3, 9, 13, 16])
y2 = np.array([2, 6, 10, 14])
plt.plot(y2, "*-.r", ms = 15, mfc ="g")
plt.xlabel("day 1")
plt.ylabel("day 2")

dict = {"text" : "data view", "fontfamily" : "sans-serif", "color" : "r","size" : 17, "fontstyle" :"italic"}
DictData = dict.get("text")
DictData = str(DictData).upper()
dict.update({"text" : DictData})
dict2 = {"text" : "day 1", "fontfamily" : "serif", "color" : "r","size" : 17, "fontstyle" :"italic"}
dict3 = {"text" : "day 2", "fontfamily" : "serif", "color" : "r","size" : 17, "fontstyle" :"italic"}

DictData1 = dict2.get("text")
DictData1 = str(DictData1).upper()
dict2.update({"text" : DictData1})

DictData2 = dict3.get("text")
DictData2 = str(DictData2).upper()
dict3.update({"text" : DictData2})
plt.title(dict["text"], fontdict=dict, loc= "left")
plt.xlabel(dict2["text"], fontdict=dict2, loc="right")
plt.ylabel(dict3["text"],fontdict=dict3, loc="top" )

plt.grid(axis= "x", c= "m", ls = ":", lw ="2.5")
plt.grid(axis = "y", c = "b", ls = "--", lw= "2.5")
plt.show()
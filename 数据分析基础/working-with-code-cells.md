
# 操作代码单元格

在这个 notebook 中，你将尝试操作代码单元格。

首先，运行以下代码单元格。就像之前我所提到的，你可以通过选中并点击运行（run cell）按钮来运行代码单元格。另外，你也可以通过快捷键 **Shift + Enter** 来运行。使用快捷键的好处是你的双手不需要离开键盘。


```python
# 选中单元格，并按 Shift + Enter
3**2
```

Shift + Enter 运行单元格之后会自动选中下一个单元格，或者根据需要创建新的单元格。你也可以通过 **Control + Enter** 在运行之后仍然选中当前单元格。

单元格中的代码运行的结果将会显现在单元格下方。它和正常的 Python shell 一样打印出代码的运行结果，但是只会打印最后一个运行结果。如果你想打印所有结果，你需要使用 `print()` 。

> **练习：** 运行下方两个代码单元格测试以上所学内容。先预测你的猜想，然后运行它。


```python
3**2
4**2
```


```python
print(3**2)
4**2
```

现在尝试将值赋予变量。


```python
mindset = 'growth'
```

这行代码没有任何输出 `'growth'` 已被赋值给变量 `mindset`。所有在单元格创建的变量，函数和类都可以在当前 Notebook 中的其它单元格访问。

你觉得运行如下单元格将会得到什么结果？尝试改变它的不同形式来熟悉这种使用方法。


```python
mindset[:4]
```

## 代码补全

当你在写代码的时候，你将发现代码补全可以大大节省你使用变量或者函数的时间，因为你只需要键入名称的一部分，然后按 **tab** 。

> **练习：** 将你的鼠标点击到 `mind` 最后，并按 **tab**


```python
mind
```

这里，补全 `mind` 将显示出整个变量名 `mindset`。如果有多个变量名以相同的字母开始，则你会得到一个下拉菜单，可以通过以下例子加深理解。


```python
# Run this cell
mindful = True
```


```python
# Complete the name here again, choose one from the menu
mind
```

记住，在一个单元格中赋值的变量可以在所有单元格中访问。这包括你之前运行的单元格和变量赋值前面的单元格。尝试在往上数第三个单元格（mind）中使用代码补全。

当你想使用一个模块但不太记得你想使用的函数，或者有哪些函数可以使用，代码补充的功能将非常方便。我将通过 [random](https://docs.python.org/3/library/random.html) 模块来展示这种用法。这个模块提供了生成随机数的函数，在创建虚拟数据或从列表中随机挑选的时候特别有用。


```python
# 运行如下
import random
```

> **练习：** 在下如单元格中，将鼠标点击至 `random.` 后并按 **tab** 来触发该模块的代码补全菜单。从列表中选择 `random.randint` ，你可以使用上下键来选择。


```python
random.
```

通过以上方法你可以看到 random 模块中的所有可用函数。比如你可能在寻找从 [高斯分布](https://en.wikipedia.org/wiki/Normal_distribution)中生成随机数的方法。高斯分布又称为“正态分布”或者“钟曲线”。

## 工具使用建议

你看到有一个函数叫作 `random.gauss` 但如何使用它呢？你可以点击 [文档](https://docs.python.org/3/library/random.html)，或者直接在 notebook 中查看。

> **练习：** 在如下单元格中，将鼠标点击至 `random.gauss` 并按 **shift + tab** 显示使用建议。


```python
random.gauss
```

你将看到类似如下的简单的文档内容：

    Signature: random.gauss(mu, sigma)
    Docstring:
    Gaussian distribution.
    
该函数需要两个参数 `mu` 和 `sigma`。这是高斯分布中均值和标准差的标准符号。可能你现在还不熟悉，但你需要了解这些参数所代表的意思。类似的情况会经常发现，你找到一个函数，但你需要知道更多的信息。你可以按 **shift + tab** 两次显示更多的信息。

> **练习：** 在如下代码单元格中，通过按两次 **shift + tab** 显示全部文档。


```python
random.gauss
```

你将看到类似如下的更加详细的信息：

    mu is the mean, and sigma is the standard deviation.  This is
    slightly faster than the normalvariate() function.

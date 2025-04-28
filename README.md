# Time-Countdown-App
## CountdownApp
CountdownApp 是一个基于 Python 的倒计时应用程序，提供定时提醒功能。它包含一个 90 分钟的倒计时周期，每隔 3-5 分钟触发一次 10 秒的全屏倒计时，并在 90 分钟后触发一个 20 分钟的全屏倒计时。目前支持 Python 脚本和 macOS 应用程序，未来计划开发 Android 版本。（目前app十分简陋且不完善，且只适用于PC，Mac，其中PC需要手动执行Python脚本）
## 目录

- 使用 Python 脚本
- 安装 Mac 应用程序
- 应用程序界面与功能
- 未来计划

### 使用 Python 脚本
前提条件

Python 3.6 或更高版本：从 python.org 下载并安装。
无需额外库，脚本使用 Python 标准库（tkinter、time、threading、random）。

步骤

克隆仓库：
git clone https://github.com/Leeye1/Time-Countdown-App.git

cd Python

运行脚本：
python3 countdown_app.py

这将启动带有图形界面的应用程序。

操作应用程序：参见 应用程序界面与功能 了解如何使用。


### 安装 Mac 应用程序
前提条件

macOS 系统（已在 macOS 10.15 及以上版本测试）。

步骤

克隆仓库：
git clone https://github.com/Leeye1/Time-Countdown-App.git

cd Time-Countdown-App


找到应用程序：

CountdownApp.app 位于仓库的MAC App目录。

安装应用程序：

将 CountdownApp.app.zip解压 复制或移动到 /Applications 文件夹

双击 /Applications/CountdownApp.app 运行。


### 应用程序界面与功能
应用程序包含两个主要界面：
1. 初始界面

按钮：
开始倒计时：启动 90 分钟倒计时，并切换到倒计时界面。
关闭：立即退出应用程序。


用途：这是启动倒计时序列的入口。

2. 倒计时界面

显示：以 MM:SS 格式显示 90 分钟倒计时（从 90:00 到 00:00）。
按钮：
关闭：停止倒计时，取消所有计划的全屏倒计时，并返回初始界面。


周期性倒计时：
每隔 3-5 分钟（随机间隔），会出现一个全屏的 10 秒倒计时。
每次 10 秒倒计时结束后，下一个 10 秒倒计时将在 3-5 分钟后重新触发。


最终倒计时：
90 分钟后，触发一个全屏的 20 分钟倒计时。
20 分钟倒计时结束后，应用程序自动退出。



注意事项
在倒计时界面点击“关闭”后，应用程序会重置到初始界面，允许重新开始倒计时。

### 未来计划

Android 应用程序：可能计划开发 Android 版本的 CountdownApp，使其可在移动设备上使用。
附加功能：未来可能添加可自定义的倒计时间隔、视觉主题和倒计时声音提醒。


欢迎贡献和反馈！请在 GitHub 上提交问题或拉取请求。

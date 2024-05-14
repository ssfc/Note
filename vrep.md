# v-rep教程

https://www.bilibili.com/video/BV1kS4y1G7Ct/?p=2&spm_id_from=pageDriver&vd_source=3ef4175721f926fbf390a069da19b0ca

ep 2, 界面介绍。查看系统样例。三视图。v-rep怎么关闭打开的scene?    add 添加。     调整大小。   Item shift.   直接拖动；  赋值坐标（大地坐标）；Translation是相对移动。运行后空中的球会掉下来。旋转同理。(2024年5月9日)

ep 3, 四连杆仿真。

ep 4, dummy设定情况。

ep 5, 仿真编程说明。

### Q: v-rep中的dummy是什么？

在V-REP（现在被称为CoppeliaSim）中，“dummy”是一种虚拟的辅助对象（visual helper object），用途非常广泛。虽然它自身不直接参与仿真的物理计算，但dummy可作为参照点、目标位置或路径点等重要的辅助元素在多种场景中发挥作用。它是设计和运行仿真过程中一个极其有用的组件。

Dummy的主要用途包括：

1. **参考和对齐对象**：在复杂的模拟环境中，dummy可以作为参考点或标记，帮助用户在场景中定位或对齐其他对象。

2. **代表目标位置或路径点**：在路径规划和移动仿真中，dummy可以标示预定的目标位置或路径点使移动的对象（如机器人）可以向这些点移动。

3. **作为传感器的检测点**：某些类型的传感器，如接近传感器或视觉传感器，可能需要特定的点来检测。dummy可以作为这些检测任务的目标点。

4. **机械连接的辅助**：在需要定义对象之间的机械连接（如关节、弹簧连接等）的场景中，dummy可以用来精确定义连接的位置和方向。

5. **逆向运动学（IK）的关键点**：在实现逆向运动学时，dummy对象常用作IK链条的目标点，引导机械臂或其他连动结构向期望的位置或姿态运动。

特点：

- **不参与物理仿真**：dummy对象本身不具备质量或物理属性，因此不直接参与物理仿真计算。
- **可视化与隐藏**：根据需要，dummy对象在仿真过程中可以可视化或隐藏，不影响其它仿真元素。
- **可链接到其他对象**：dummy可以链接到场景中的其他对象，以此来建立一种逻辑或空间上的关系。

由于上述特性，dummy在CoppeliaSim（V-REP）的仿真项目中扮演着非常重要的角色，尽管它看起来简单，但在设计和执行仿真时具有极大的灵活性和应用价值。

### Q: v-rep中能否设置物体的加速度？

在V-REP（现称为CoppeliaSim）中，直接设置物体的加速度并不是一个内置的功能。这是因为物理引擎通常是基于力和扭矩来动态模拟物理对象的运动的。物体的加速度是由施加在物体上的力和物体的质量共同决定的（根据牛顿第二定律）。然而，您可以通过一些方法间接控制或模拟加速度的效果。

要模拟加速度，您可以按照以下几种方法之一来操作：

1. **动态计算并应用力**：您可以编写脚本来动态计算并在每个仿真步骤中应用所需的力，以产生期望的加速度。根据牛顿第二定律（F=ma），您可以根据物体的质量和想要的加速度来计算需要施加的力。这种方法可以让您精确地控制物体的加速过程。

2. **使用动力学属性**：您可以通过调整物体的动力学属性（例如，马达的速度或扭矩，或者是通过设置关节的目标速度）来间接实现加速度效果。这要求您有一个对动力系统结构较好的理解，以便能够设置适当的参数以达到期望的加速度行为。

3. **编写自定义控制脚本**：您可以使用CoppeliaSim支持的脚本语言（例如Lua）来开发自定义的控制策略，这通过控制每个仿真步骤中的物体速度或施加的力来实现加速度控制。例如，您可以计算出要在特定时间内达到特定速度所需要的平均加速度，然后使用这个加速度值来确定每个仿真步骤需要施加的力。

示例Lua脚本

下面是一个简单的Lua脚本示例，展示了如何在CoppeliaSim中根据指定的加速度和质量来计算并施加力：

```lua
function sysCall_init()
    objectHandle = sim.getObjectHandle("ObjectName") -- 获取物体的句柄
    mass = sim.getShapeMassAndInertia(objectHandle) -- 获取物体的质量
    acceleration = 1.0 -- 设定加速度（单位：m/s^2）
end

function sysCall_actuation()
    force = mass * acceleration -- 计算需要施加的力
    sim.addForce(objectHandle, {0,0,force}, {0,0,0}) -- 在物体的Z轴施加力
end
```
请注意，您需要将"ObjectName"替换为场景中物体的实际名称，并且可能需要根据物体当前的方向和加速度方向施加力。

总之，尽管CoppeliaSim不直接提供设置加速度的接口，但通过脚本控制施加的力量，您可以实现对物体加速度的有效模拟和控制。

ep 6, 传送带模型创建。

### Q: v-rep能否从外部导入JSON格式的轨道地图数据？

截至我最后更新的信息，在V-REP（现称为CoppeliaSim）中并没有内置直接支持从外部导入JSON格式轨道地图数据的功能。CoppeliaSim是一个非常灵活和强大的机器人仿真平台，它提供了丰富的API接口和脚本功能，可以通过编写代码来实现对各种数据格式的读取和解析，包括JSON。

若要将JSON格式的轨道地图数据导入到CoppeliaSim中，你可以采用以下步骤：

1. **解析JSON**：首先，你需要解析JSON文件。这可以通过编写一个脚本来完成，脚本可以使用Lua或任何CoppeliaSim支持的扩展语言（如果你使用的是带有Python接口的CoppeliaSim版本，Python对JSON的支持将非常有用）。

2. **读取地图数据**：解析JSON文件后，提取你需要的地图数据，如轨道的位置、方向、长度等信息。

3. **在CoppeliaSim中创建地图**：使用解析得到的地图数据，在CoppeliaSim中创建对应的场景对象。这可能涉及到创建路径点、轨道和其他必要的场景元素。如果轨道可以由简单的几何形状组成，你可以通过编程方式创建这些形状并按照轨道的位置和方向摆放它们。

具体到实现上，这里是一个大致的示例流程，基于假设你正在使用Lua脚本来处理JSON数据：

1. 使用一个外部库解析JSON数据

Lua本身没有内置对JSON的支持，所以你需要使用一个Lua的JSON库。例如，你可以使用`dkjson`库，你需要确保这个库与你的脚本在同一目录下或在Lua的包路径中。

```lua
local json = require("dkjson")

-- 假设你的JSON数据是关于轨道的，存在于一个文件中
local path = 'your_track_data.json'
local file = io.open(path, "r")
local data = file:read("*a") -- 读取整个文件内容
file:close()

local trackData, pos, err = json.decode(data, 1, nil)
if err then
  print("Error:", err)
else
  -- 这里处理你的地图数据
  print(trackData)
end
```

2. 根据JSON中的数据创建场景对象

```lua
-- 基于trackData创建路径或轨道
for i, track in ipairs(trackData.tracks) do
    -- 假设每个轨道有其起点和终点，你可以据此创建路径或其他代表轨道的对象
    local startPoint = track.startPoint
    local endPoint = track.endPoint
    -- 使用CoppeliaSim的API创建场景对象，例如，线段、路径或自定义形状等
end
```

请注意，具体的实现会非常依赖于你的项目需求以及JSON数据的结构。这个示例只是一个很高级的示范，实际应用中你需要根据你的轨道地图数据的具体格式来调整数据处理和对象创建的代码。

如果你不熟悉Lua脚本或需要更复杂的数据处理，也可以考虑使用外部程序处理JSON并以CoppeliaSim可以识别的格式（如其自己的场景文件格式）输出，然后再导入到CoppeliaSim中。

ep 7, 传送带编程。

ep 8, 传送带两种方式合并及区别说明。

ep 9, 小车模型建立。这个视频的文件在C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\scenes\tutorials。

一个大球作为车体，两个圆柱作为后轮，两个圆柱作为轴承，一个球体作为前轮。(2024年5月9日)

ep 10, 小车简单避障编程实现。

如果需要碰撞检测，需要勾上Collidable, Measurable和Detectable. (2024年5月13日)

### Q: V-REP中的local respondable mask和global respondable mask是什么意思？

在V-REP中，local respondable mask和global respondable mask是用来控制物体之间碰撞检测的一种机制。它们定义了每个物体与其他物体之间的碰撞检测的规则。

1. **Local Respondable Mask（局部响应掩码）**：
   - 局部响应掩码定义了物体与其周围其他物体之间的碰撞检测规则。
   - 每个物体都有一个局部响应掩码，它由一组位标志（bit flags）组成，每个位标志代表一个物体的响应情况。
   - 例如，如果第i位标志被设置为1，则表示物体会与具有相同位标志设置的其他物体发生碰撞，否则不会发生碰撞。

2. **Global Respondable Mask（全局响应掩码）**：
   - 全局响应掩码定义了整个场景中所有物体之间的碰撞检测规则。
   - 它通常由一组位标志组成，与局部响应掩码类似，但它适用于所有物体。
   - 全局响应掩码的设置影响所有物体之间的碰撞检测规则，因此可以用于全局性的碰撞检测控制。

通过设置局部响应掩码和全局响应掩码，用户可以灵活地控制物体之间的碰撞检测规则，从而实现各种复杂的碰撞行为和模拟效果。

ep 11, 寻迹灯的建立。

Vision sensor是可以识别颜色的摄像头，设置识别最大最小距离。检测灯在地面下也有探测距离。(2024年5月13日)

ep 12, 寻迹线的建立。

过去的路径编辑器被整合到主scene里面了。(2024年5月13日)

直线用来做非封闭的曲线，圆用来做封闭的曲线。(2024年5月13日)

ep 13, 寻迹原理。

路径线不是和地板重合，而是比地板稍高一点点。(2024年5月13日)

## 范例scene文件说明

### 主文件夹

collisionDetectionDemo-lua.ttt。collisionDetectionDemo-lua.ttt是V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了如何使用Lua脚本来进行碰撞检测和响应。// 在collisionDetectionDemo-lua.ttt示例场景中，你可以看到一个包含多个物体的环境模型，以及一个用于控制机器人的Lua脚本。该示例演示了如何在V-REP中使用Lua脚本来检测物体之间的碰撞，并根据碰撞情况采取相应的行动。// 示例场景中的Lua脚本通常包含以下功能：1. **碰撞检测**：通过检测机器人与其他物体之间的碰撞来确定碰撞状态。2. **碰撞响应**：根据碰撞检测结果，采取相应的行动来避免碰撞或处理碰撞情况。这可能包括改变机器人的运动方向、速度或停止运动等。// 通过collisionDetectionDemo-lua.ttt示例场景，你可以学习如何在V-REP中使用Lua脚本来实现碰撞检测和响应功能。这对于开发机器人控制算法、避障算法等非常有帮助。(2024年5月10日)

collisionDetectionDemo-python.ttt 。python版本。

customUI-lua.ttt。customUI-lua.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了如何使用 Lua 脚本来创建自定义用户界面（Custom User Interface）。// 在 customUI-lua.ttt 示例场景中，你可以看到一个包含一个简单机器人模型和一些控件的用户界面。通过 Lua 脚本，用户可以与这些控件进行交互，并控制机器人的行为。// 示例场景中的 Lua 脚本通常包含以下功能：1. **创建界面**：通过 Lua 脚本创建用户界面，包括按钮、滑块、文本框等控件。2. **添加交互功能**：为界面中的控件添加交互功能，例如按钮点击事件、滑块数值变化事件等。3. **控制机器人**：根据用户界面的操作，控制机器人的运动、动作等。// 通过 customUI-lua.ttt 示例场景，你可以学习如何在 V-REP 中使用 Lua 脚本创建自定义用户界面，并实现与场景中模型的交互。这对于开发交互式仿真场景、用户界面设计等非常有帮助。(2024年5月10日)

customUI-python.ttt。是Python版。(2024年5月10日)

eulerAngles-lua.ttt。eulerAngles-lua.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了如何使用 Lua 脚本来控制机器人的欧拉角（Euler Angles）姿态。// 在 eulerAngles-lua.ttt 示例场景中，你可以看到一个简单的机器人模型，以及一些控制界面。通过 Lua 脚本，用户可以通过控制界面上的按钮来改变机器人的欧拉角姿态。// 示例场景中的 Lua 脚本通常包含以下功能：1. **获取和设置欧拉角**：通过 Lua 脚本获取机器人当前的欧拉角姿态，并根据用户的操作来修改姿态。2. **控制机器人姿态**：根据用户界面上的按钮点击事件，调整机器人的姿态，例如改变机器人的旋转角度、姿态方向等。// 通过 eulerAngles-lua.ttt 示例场景，你可以学习如何在 V-REP 中使用 Lua 脚本来控制机器人的姿态。这对于开发机器人控制算法、姿态控制器等非常有帮助。(2024年5月10日)

eulerAngles-python.ttt。是Python版。(2024年5月10日)

fabricationBlocks.ttt。fabricationBlocks.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了一个基于模块化部件的制造流程。// 在 fabricationBlocks.ttt 示例场景中，你可以看到一系列模块化的部件（例如方块、圆柱等），以及一个机器人模型和一些生产线设备。这个示例场景演示了机器人如何从模块化的部件中组装产品，并将其放置在指定位置。// 示例场景中的机器人通常会执行以下操作：1. **获取部件**：机器人会从生产线上获取模块化的部件，例如方块或圆柱。2. **组装产品**：机器人会根据预定的流程和顺序，将不同的部件组装成产品。这可能涉及到物体的移动、旋转、连接等操作。3. **放置产品**：一旦产品组装完成，机器人会将其放置在指定的位置，例如装配线上的下一道工序。// 通过 fabricationBlocks.ttt 示例场景，你可以学习如何在 V-REP 中模拟和仿真制造流程，以及如何使用机器人来执行产品的组装和生产任务。这对于学习制造流程规划、自动化生产等非常有帮助。(2024年5月10日)

gCode.ttt。gCode.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了如何使用 G 代码（G-code）控制机器人执行任务。// 在 gCode.ttt 示例场景中，你可以看到一个机器人模型和一些控制界面。通过 G 代码，用户可以编写和执行一系列指令，控制机器人执行特定的动作和任务。// G 代码是一种用于控制**数控机床**和其他自动化设备的编程语言。它由一系列指令组成，用于指导机器人执行各种操作，例如移动、旋转、加工等。在 gCode.ttt 示例场景中，用户可以通过编写和执行 G 代码，来控制机器人执行特定的动作和任务，例如移动到指定位置、执行特定的动作序列等。// 通过 gCode.ttt 示例场景，你可以学习如何在 V-REP 中使用 G 代码来控制机器人执行任务。这对于学习数控编程、机器人编程等非常有帮助。(2024年5月10日)

gears.ttt。gears.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了齿轮系统的运动学和动力学仿真。// 在 gears.ttt 示例场景中，你可以看到一个包含多个齿轮的机械系统模型。这些齿轮通过齿轮传动相互连接，当一个齿轮转动时，其它齿轮也会受到影响而转动。// 示例场景中的齿轮系统模型通常会考虑以下因素：1. **齿轮之间的传动关系**：每个齿轮的大小、齿数和排列方式对齿轮之间的传动关系产生影响，从而影响整个系统的运动。2. **动力学效应**：齿轮系统的运动不仅受到外部输入的影响，还受到内部摩擦、惯性等动力学效应的影响，因此需要考虑这些效应对系统运动的影响。// 通过 gears.ttt 示例场景，你可以学习如何在 V-REP 中建模和仿真齿轮系统，以及如何分析齿轮系统的运动学和动力学行为。这对于学习机械系统建模、运动学分析和动力学仿真等非常有帮助。(2024年5月10日)

hapticRobot.ttt。hapticRobot.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了使用触觉反馈技术（Haptic Feedback）控制机器人的交互式仿真。// 在 hapticRobot.ttt 示例场景中，你可以看到一个包含一个机器人模型和一个触觉设备（可能是力反馈手柄或力觉传感器）的环境。通过触觉设备，用户可以与仿真场景进行交互，并感受到机器人运动时的力反馈。// 示例场景中的机器人通常会执行一些任务，例如在环境中移动物体、执行操作等。当用户通过触觉设备控制机器人时，他们可以感受到机器人在仿真环境中的力和运动，并根据反馈调整其行为。// 通过 hapticRobot.ttt 示例场景，你可以学习如何在 V-REP 中模拟和仿真触觉反馈技术，并探索交互式仿真的应用。这对于研究人机交互、虚拟现实、远程操作等领域非常有帮助。(2024年5月10日)

iglDemo-lua.ttt吗？iglDemo-lua.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了如何使用 Lua 脚本结合 Interactive Graphical Lua（IGL）库创建交互式的图形用户界面（GUI）。// 在 iglDemo-lua.ttt 示例场景中，你可以看到一个包含一些基本控件（如按钮、滑块、文本框等）的图形界面，以及一个机器人模型。通过 Lua 脚本和 IGL 库，用户可以与这些控件进行交互，并控制机器人的运动和行为。// IGL 是一个用于创建图形用户界面的 Lua 库，它提供了一系列函数和工具，用于创建和管理 GUI 控件，并实现与控件的交互。通过 iglDemo-lua.ttt 示例场景，你可以学习如何使用 Lua 脚本和 IGL 库来创建自定义的图形界面，并将其集成到 V-REP 的仿真环境中。这对于开发交互式仿真场景、用户界面设计等非常有帮助。(2024年5月10日)

iglDemo-python.ttt。是Python版。(2024年5月10日)

minimumDistanceCalculationDemo-lua.ttt。minimumDistanceCalculationDemo-lua.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了如何使用 Lua 脚本计算机器人与障碍物之间的最小距离。// 在 minimumDistanceCalculationDemo-lua.ttt 示例场景中，你可以看到一个包含一个机器人模型和一些障碍物的环境。通过 Lua 脚本，机器人可以计算自身与周围障碍物的最小距离，并根据距离值采取相应的行动。// 示例场景中的 Lua 脚本通常包含以下功能：1. **检测障碍物**：通过感知或碰撞检测，机器人可以获取周围障碍物的位置和形状信息。2. **计算最小距离**：根据障碍物的位置和机器人的当前位置，计算机器人与障碍物之间的最小距离。3. **决策行动**：根据计算得到的最小距离值，机器人可以决定采取何种行动，例如避障、停止运动等。// 通过 minimumDistanceCalculationDemo-lua.ttt 示例场景，你可以学习如何使用 Lua 脚本计算机器人与障碍物之间的最小距离，并根据距离值实现智能决策和行动。这对于开发自主导航、避障算法等非常有帮助。(2024年5月10日)

minimumDistanceCalculationDemo-python.ttt。是Python版。(2024年5月10日)

**mobileRobotVisualTraces-lua.ttt**。mobileRobotVisualTraces-lua.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了如何使用 Lua 脚本为移动机器人生成轨迹并进行可视化。// 在 mobileRobotVisualTraces-lua.ttt 示例场景中，你可以看到一个移动机器人模型和一些障碍物，以及一个地图或场景背景。通过 Lua 脚本，移动机器人可以在仿真环境中移动，并在地图上留下运动轨迹的可视化表示。// 示例场景中的 Lua 脚本通常包含以下功能：1. **移动机器人控制**：通过控制机器人的轮子或关节，使其在仿真环境中移动。2. **轨迹生成**：在机器人移动过程中，通过记录其位置信息，生成轨迹数据。3. **可视化表示**：使用图形绘图功能，将轨迹数据在地图或场景上进行可视化表示，以便用户观察和分析。// 通过 mobileRobotVisualTraces-lua.ttt 示例场景，你可以学习如何使用 Lua 脚本为移动机器人生成轨迹并进行可视化，这对于机器人路径规划、运动控制和仿真分析非常有帮助。(2024年5月10日) => 两轮小车，具有避障功能，并且显示轨迹。**f**。(2024年5月10日)

**motorControllerExamples-lua.ttt**。This scene features various dynamic motor controllers available in CoppeliaSim: 

1. constant force/torque (in red)

2. velocity (in green), or velocity with specific motion profile (in light green)

3. position (in blue), or position with specific motion profile (in light blue)

5. spring-damper mode (in purple)

5. custom control (in yellow) enables virtually any type of controller via joint callback functions(2024年5月10日) => 可以控制速度、力、时间。**可能用于AMHS**。(2024年5月10日)

mobileRobotVisualTraces-python.ttt。是Python版。(2024年5月10日)

mouseTestScene.ttt。mouseTestScene.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景用于演示如何使用鼠标进行交互式操作。// 在 mouseTestScene.ttt 示例场景中，你可以看到一个环境模型和一个机器人模型。通过鼠标，用户可以与仿真环境进行交互，例如选择物体、移动物体、改变视角等操作。// 示例场景中的主要功能可能包括：1. **选择物体**：用户可以使用鼠标点击来选择仿真环境中的物体，以便进行操作或查看其属性。2. **移动物体**：通过鼠标拖拽，用户可以移动选择的物体到新的位置。3. **改变视角**：用户可以通过鼠标移动来改变视角，从不同的角度观察仿真场景。// 通过 mouseTestScene.ttt 示例场景，用户可以学习如何在 V-REP 中实现鼠标交互功能，这对于开发交互式仿真场景和用户界面设计非常有帮助。(2024年5月10日)

**movingAlongAPath-lua.ttt**。可以让物体沿指定路径移动。(2024年5月10日) => **可能用于AMHS**。(2024年5月10日)

movingAlongAPath-python.ttt。是Python版。(2024年5月10日)

navigationWithinAPointCloud-lua.ttt。是V-REP（Virtual Robot Experimentation Platform）中一个示例场景文件。这个场景演示了如何在点云数据中进行导航。// 点云（PointCloud）是一种三维空间中离散点的集合，通常用于表示物体表面或环境的几何形状。navigationWithinAPointCloud-lua.ttt场景利用点云数据来模拟环境，并演示了一个机器人在点云数据中进行导航的过程。// 在这个示例场景中，你可以看到一个机器人模型和一个包含点云数据的环境模型。机器人需要根据点云数据来规划路径，并在环境中移动。示例场景演示了如何使用Lua脚本来实现机器人的路径规划和导航算法，以及如何利用点云数据进行环境感知和障碍物避开。// 通过导航WithinAPointCloud-lua.ttt示例场景，你可以学习如何在V-REP中使用点云数据进行机器人导航，以及如何编写Lua脚本来实现自定义的导航算法。这对于学习和理解机器人导航技术非常有帮助。(2024年5月10日)

navigationWithinAPointCloud-python.ttt。是Python版。(2024年5月10日)

**octreeGenerationDemo.ttt**。octreeGenerationDemo.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了如何使用八叉树（Octree）生成环境模型。// 在 octreeGenerationDemo.ttt 示例场景中，你可以看到一个环境模型，可能包含一些障碍物或物体。通过八叉树生成算法，可以将环境模型分割成多个立方体（或八叉树节点），以便于表示和处理。// 示例场景中的八叉树生成算法通常包括以下步骤：1. **环境建模**：首先，需要对环境进行建模，包括记录环境中的障碍物、物体等信息。2. **八叉树分割**：然后，通过八叉树生成算法，将环境模型进行分割，生成八叉树结构。3. **节点表示**：每个八叉树节点代表一个立方体区域，包含该区域内的环境信息（如障碍物、物体等）。4. **可视化显示**：最后，将生成的八叉树结构可视化显示在仿真环境中，以便用户观察和分析。// 通过 octreeGenerationDemo.ttt 示例场景，你可以学习如何使用八叉树生成算法对环境模型进行分割和表示，这对于机器人感知、碰撞检测、路径规划等应用非常有帮助。(2024年5月10日) => 三轮小车，具有避障功能，在迷宫中寻路。(2024年5月10日) => 可以调研一下这里用到的八叉树算法。**可能用于AMHS**。(2024年5月10日)

pickAndPlaceDemo.ttt。pickAndPlaceDemo.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了如何使用机器人进行物体的抓取和放置操作。// 在 pickAndPlaceDemo.ttt 示例场景中，你可以看到一个包含一个机器人模型、物体和工作台（或其它表面）的环境。通过仿真中的机器人，可以演示物体抓取和放置的操作流程。// 示例场景中的主要步骤可能包括：1. **定位物体**：机器人需要通过视觉或其他感知手段定位要抓取的物体的位置。2. **抓取物体**：机器人通过控制夹爪或末端执行器，将手臂移动到目标位置，并进行物体的抓取动作。3. **运输物体**：机器人将抓取到的物体从初始位置运输到目标位置。4. **放置物体**：机器人通过控制手臂，将物体放置在目标位置上。// 通过 pickAndPlaceDemo.ttt 示例场景，你可以学习如何在 V-REP 中实现机器人的抓取和放置操作，这对于工业机器人应用、自动化生产线设计等领域非常有帮助。(2024年5月10日)

proximitySensorDemo.ttt。proximitySensorDemo.ttt 是 V-REP（Virtual Robot Experimentation Platform）中的一个示例场景文件。这个场景演示了如何使用接近传感器（Proximity Sensor）进行环境感知和障碍物检测。// 在 proximitySensorDemo.ttt 示例场景中，你可以看到一个包含机器人模型和一些障碍物的环境。通过仿真中的接近传感器，可以模拟机器人对周围环境进行感知，并检测障碍物的位置和距离。// 示例场景中的主要功能可能包括：1. **接近传感器设置**：在机器人的适当位置安装接近传感器，并设置传感器的检测范围和参数。2. **障碍物检测**：通过接近传感器检测周围环境中的障碍物，包括墙壁、物体等。3. **距离测量**：接近传感器可以测量障碍物与机器人之间的距离，并将距离信息传递给控制系统进行处理。4. **碰撞避免**：根据接近传感器检测到的障碍物信息，机器人可以采取相应的措施，避免与障碍物发生碰撞。// 通过 proximitySensorDemo.ttt 示例场景，你可以学习如何使用接近传感器进行环境感知和障碍物检测，这对于自主导航、避障算法和安全控制非常有帮助。(2024年5月10日) => 一个蜘蛛机器人通过感知进行运动。(2024年5月10日)

proximitySensorDemo2.ttt也差不多。(2024年5月10日)

rendererDemo.ttt。一个机械臂搬运箱子。(2024年5月10日)

robotLanguageControl.ttt。机械臂抓取传送带物品。(2024年5月10日)

RRS-1 demo.ttt吗？显示不成功。(2024年5月10日)

sceneObjectIndependentGeometricCalculationExample.ttt。衡量两个运动物体之间的距离。(2024年5月10日)

simpleThreadedAndNonThreadedExample-lua.ttt。看起来像一堆字幕跑了。(2024年5月10日)

simpleThreadedAndNonThreadedExample-python.ttt。是Python版。(2024年5月10日)

teleportDynamicModel.ttt。小蜘蛛爬来爬去。(2024年5月10日)

ur5WithRg2Grasping-lua.ttt。机械臂抓起立方体并横放。(2024年5月10日)

ur5WithRg2Grasping-python.ttt。是Python版。(2024年5月10日)

workspace.ttt。笼罩了一个圆球。(2024年5月10日)

youBotAndHanoiTower.ttt。机械臂把立方体放到托盘上并搬运。(2024年5月10日)

### 文件夹awsRobomaker。

aws_robomaker_house.ttt。一个有各种家具的大房间。(2024年5月10日)

aws_robomaker_warehouse.ttt。一个有架子的大仓库。(2024年5月10日)

### 文件夹controlTypeExamples

controlledViaPlugin.ttt 三轮小车，具有避障功能，躲避几个静态立方体障碍物。(2024年5月10日) => **可能用于AMHS**。(2024年5月10日)

controlledViaRos.ttt 估计是通过ROS控制。(2024年5月10日) => **可能用于AMHS**。(2024年5月10日)

controlledViaRemoteApi.ttt 三轮小车，具有避障功能，躲避几个静态立方体障碍物。(2024年5月10日) => 猜测可能是通过远程API控制，这个可能仿真用得到，因为吾人就是给小车远程下令的。(2024年5月10日) => **可能用于AMHS**。(2024年5月10日)

controlledViaRos2.ttt 估计是另一种ROS控制。(2024年5月10日) => **可能用于AMHS**。(2024年5月10日)

controlledViaScript.ttt 三轮小车*3，具有避障功能，躲避几个静态立方体障碍物。(2024年5月10日) => 猜测是通过脚本控制，这个可能仿真用得到，因为吾人可以把轨迹写成script，交给小车执行。(2024年5月10日) => **可能用于AMHS**。(2024年5月10日)

controlledViaTcp.ttt 估计是通过网络控制。(2024年5月10日) => **可能用于AMHS**。(2024年5月10日)

controlledViaZmq.ttt。通过zmq控制。(2024年5月10日) => **可能用于AMHS**。(2024年5月10日)

### 文件夹kinematics

abbFantaCanChallenge.ttt。托盘机器人。

ikPathGeneration.ttt。活动关节的机械臂产生了轨迹。(2024年5月10日)

nDoFKinematicChain.ttt。一根竖直的棒子。(2024年5月10日)

obstacleAvoidanceAndIk.ttt。多个小球彼此避障。(2024年5月10日)

smoothMovementsInFkAndIk.ttt。一个操纵杆平滑移动小球，并生成轨迹。(2024年5月10日)

twoRobotsIK.ttt。两个robot面对面。(2024年5月10日)

#### 子文件夹simpleExamples

1-singleIkGroupWithSingleIkElement-undamped.ttt计算 IK链条。(2024年5月10日)

2-singleIkGroupWithSingleIkElement-damped.ttt 也是计算IK. (2024年5月10日)

3-singleIkGroupWithTwoIkElements.ttt 估计也是计算IK。(2024年5月10日)

4-singleIkGroupWithTwoIkElements-weightedAndDampedResolution.ttt 估计也是计算IK。(2024年5月10日)

5-twoIkGroupsWithEachOneIkElement-resolutionOrderIsNotRelevant.ttt 估计也是计算IK。(2024年5月10日)

6-twoIkGroupsWithEachOneIkElement-resolutionOrderIsRelevant.ttt 估计也是计算IK。(2024年5月10日)

7-fkAndIkResolutionForParallelMechanisms.ttt 果然也是计算IK。(2024年5月10日)

8-computingJointAnglesForRandomPoses.ttt 计算连接的关节。(2024年5月10日)

9-prioritizedGroupsAndNullSpaceProjection.ttt 也是计算关节。(2024年5月10日)

10-visuallyDebuggingIkGroups.ttt 也是计算关节。(2024年5月10日)

### 文件夹messaging

1     connectingTwoCoppeliaSimInstances.ttt。但见三行文字越跑越远。(2024年5月10日)

2     movementViaRemoteApi.ttt。This scene illustrates movement generation via the ZeroMQ remote API. (2024年5月10日)

3     pControllerViaRemoteApi.ttt。This scene illustrates an external motor controller via the ZeroMQ remote API. (2024年5月10日)

4     ros2InterfaceTopicPublisherAndSubscriber-lua.ttt。一堆形状各异的立方体移动。(2024年5月10日)

5     ros2InterfaceTopicPublisherAndSubscriber-python.ttt。是Python版。(2024年5月10日)

rosInterfaceTopicPublisherAndSubscriber-lua.ttt。一个探照灯转来转去。(2024年5月11日)

rosInterfaceTopicPublisherAndSubscriber-python.ttt。是Python版。(2024年5月10日)

6     synchronousImageTransmissionViaRemoteApi.ttt。This scene illustrates image transmissing via the ZeroMQ remote API. (2024年5月10日)

7     zeromqDemo-lua.ttt。看来通过ZeroMQ通信的是真的多。(2024年5月10日)

8  zeromqDemo-python.ttt。是Python版。(2024年5月10日)

### mujoco文件夹

compositeAndOtherCallbacks.ttt。This scene illustrates how composites and other XML injections can be dynamically updated during simulation。(2024年5月10日)

stringsRopesClothsAndSoftBodies.ttt。This scene features various specificities of the Mujoco engine, and thus, will not run as expected with a different engine. (2024年5月10日) => 测试Mujoco物理引擎的。

### otherScenes文件夹

1     arucoMarkerDetection.ttt。地面有些莫名其妙的图案，可能涉及图像识别。(2024年5月10日)

2     buoyancyExample.ttt。空中的小球坠落地面。(2024年5月10日)

3     dynamic4BarLinkage.ttt。一个移动的四框架。(2024年5月10日)

4     frame-frameInterpolation.ttt。坐标轴飘走了。(2024年5月10日)

5     pureTubeExtraction.ttt。管道把球吸走了。(2024年5月10日)

6     ropeTest.ttt. 滑杆经过垂绳子。(2024年5月10日)

7     simpleMagnetDemo.ttt。三轮车在墙面行走。(2024年5月10日)

8     visionSensorOverTerrain.ttt。小车在迷宫中寻路。(2024年5月10日) => **可能用于AMHS**。(2024年5月10日)

9     worm.ttt。毛毛虫蠕动。(2024年5月10日)

10   X_Y_graph_laserScanner.ttt。激光扫描探测寻路。(2024年5月10日)

### pathPlanning文件夹

1     holonomicPathPlanning3dof-lua.ttt。直角板在迷宫中寻路。(2024年5月10日)

2     holonomicPathPlanning3dof-python.ttt。估计差不多。(2024年5月10日)

3     holonomicPathPlanning6dof.ttt直角板穿过圆洞。(2024年5月10日)

mobileRobotPathPlanning.ttt。小车通过一堵墙寻路。(2024年5月10日) => **可能用于AMHS**。(2024年5月10日)

nonHolonomicPathPlanning.ttt。小车在迷宫中先寻路，再沿着轨迹行驶。(2024年5月10日) => **可能用于AMHS**。(2024年5月10日)

pathPlanningAndGrasping.ttt。两个机械臂抓起水杯互相倒水。(2024年5月11日)

roadmapMultiquery.ttt。直角板穿越迷宫。(2024年5月11日)

simpleManipulatorPathPlanning.ttt。机械臂在迷宫中扭动。(2024年5月11日)

stateValidationCallback-lua.ttt。This scene illustrates how to use a state validation callback with OMPL. The task is to bring the first 'L' onto the second 'L' while keeping a distance of at least 10 mm, and at most 25 mm from the walls. (2024年5月11日)

stateValidationCallback-python.ttt。是Python版。(2024年5月10日)

stateValidityCheckingResolution.ttt。This scene demonstrates how the choice of state validity checking resolution affects the found solutions. A too high value can produce solutions that collide with obstacles. A too low value can slow down the search. 一个球跳过墙面到达目的地。(2024年5月11日)

### trajectoryAndMotion文件夹

onlineTrajectoryGeneratorExample-lua.ttt。圆柱体上升，机械臂扭动。(2024年5月11日)

onlineTrajectoryGeneratorExample-python.ttt。是Python版。(2024年5月10日)

pathToTrajectory.ttt。This scene illustrates 3 different ways to generate a trajectory from a path (in task- or configuration space)。两个graph在显示效果。(2024年5月11日)

ruckigOnlineTrajectoryGeneratorDemo.ttt。机械臂把绿色方块移动到红色位置，把红色方块移动到绿色位置，表格显示速度和加速度。(2024年5月11日)

ruckigOnlineTrajectoryGeneratorExamples.ttt。This scene illustrates various ways to use the Ruckig Online Trajectory Generation functions available in CoppeliaSim。圆柱体绕着柱子转。(2024年5月11日)

### tutorials文件夹

#### BubbleRob文件夹

bubbleRob-lua.ttt。有避障功能的小车一堆圆柱中寻路。(2024年5月11日) => **可能用于AMHS**。(2024年5月10日)

bubbleRob-python.ttt。是Python版。(2024年5月10日)

#### BubbleRobExt文件夹

bubbleRob-lua.ttt。有避障功能的小车一堆圆柱中寻路。(2024年5月11日) => **可能用于AMHS**。(2024年5月10日)

#### InverseKinematics文件夹

redundantRobot-lua.ttt。机械臂夹着绿色的球。(2024年5月11日)

redundantRobot-python.ttt。是Python版。(2024年5月10日)

#### LineFollowingBubbleRob文件夹

lineFollowingBubbleRob-lua.ttt。有避障功能的小车一堆圆柱中寻路，然后沿着指定路线行驶。(2024年5月11日) => **可能用于AMHS**。(2024年5月10日)

lineFollowingBubbleRob-python.ttt。是Python版。(2024年5月10日)

### vision文件夹

imageProcessingDemo1-lua.ttt。机器人走路。

imageProcessingDemo1-python.ttt。是Python版。(2024年5月10日)

imageProcessingDemo2-lua.ttt。正方体在两个扇形前移来移去。（2024年5月11日）

imageProcessingDemo2-python.ttt。是Python版。(2024年5月10日)

objectTracking.ttt。一个扫地机器人在迷宫中移动。=> **可能用于AMHS**。(2024年5月10日)

ocTreeAcquiredByVisionSensor-lua.ttt。一个摄像头绕着花盆移动。(2024年5月11日)

ocTreeAcquiredByVisionSensor-python.ttt。是Python版。(2024年5月10日)

pointCloudAcquiredByVisionSensor-lua.ttt。一个摄像头绕着花盆移动。(2024年5月11日)

pointCloudAcquiredByVisionSensor-python.ttt。是Python版。(2024年5月10日)

# lineFollowingBubbleRob-lua.ttt解读

位置C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\scenes\tutorials\LineFollowingBubbleRob。视频解读https://www.bilibili.com/video/BV1kS4y1G7Ct/?p=9&vd_source=3ef4175721f926fbf390a069da19b0ca 

sensingNose中的Volume parameters设置检测区域的形状，Detection parameters可以设定检测区域。(2024年5月13日)

给场景中又添加了一辆车，两辆车都可以沿着轨迹线行驶，都可以进行碰撞检测，两台小车的速度可以分别调整。(2024年5月13日)

### Q: v-rep的path is closed是什么意思？

CG: "Path is closed" 意味着在 V-REP 中的路径（Path）对象是封闭的，也就是说路径的起点和终点相连，形成一个闭环。

在 V-REP 中，路径可以用于定义机器人或其他物体的运动轨迹。当路径被标记为封闭时，它表示路径的起点和终点相连，形成了一个闭合的循环。这通常意味着物体沿着路径移动到终点后会返回到起点，循环运动。

封闭路径在某些场景中非常有用，比如在机器人巡逻、环绕运动或循环运动中。通过使用封闭路径，可以简化路径规划和控制，使得物体可以在仿真环境中实现连续的循环运动。

因此，当 V-REP 中的路径被标记为 "Path is closed" 时，它表示路径是封闭的，可以用于定义物体的循环运动轨迹。(2024年5月12日) 

Mine: 如果去掉选框对勾，小车路径的最后一段封不起来。(2024年5月12日)

### Q: v-rep的generate extrude shape是什么意思？

CG: 在 V-REP 中，"Generate Extrude Shape" 是一个功能，用于创建一个沿着路径延伸的形状。

具体来说，"Generate Extrude Shape" 允许用户定义一个二维形状（通常是一个闭合的轮廓），然后沿着指定的路径（通常是一条直线或曲线）在三维空间中延伸该形状，生成一个复杂的三维对象。

这个功能通常用于创建具有特定截面的三维几何体，比如管道、绳索、线圈等。用户可以通过指定的路径和形状参数来控制生成的三维对象的外观和尺寸。

"Generate Extrude Shape" 功能在 V-REP 的建模工具中常用，它使用户能够快速创建复杂的三维几何体，从而实现更加真实和精确的仿真模型。

Mine: 如果不加这个对勾，小车将无视路径直接走下悬崖。(2024年5月12日)

### Q: v-rep的hidden path during simulation是什么意思？

CG: 在 V-REP 中，"Hidden path during simulation" 意味着在仿真过程中隐藏路径对象。

路径对象通常用于定义机器人或其他物体的运动轨迹。当启用 "Hidden path during simulation" 选项时，路径对象在仿真运行时将被隐藏，即不会在仿真环境中可见，但路径仍然存在于仿真场景中，并影响物体的运动。

这个功能的主要作用是提高仿真的可视化效果，减少不必要的干扰。当用户只关注物体的运动轨迹而不需要看到路径本身时，可以使用这个选项隐藏路径对象。

通过隐藏路径对象，用户可以更清晰地观察物体在仿真环境中的运动，同时减少场景中的视觉混乱，提高仿真的可视化效果。

Mine: 黑色轨迹中绿色的线条会消失。(2024年5月12日)

### Q: v-rep /Path中的Soothness数值是什么意思？

在 V-REP 中，路径（Path）对象的 Smoothness 参数表示路径的平滑程度或曲线的光滑度。该参数影响路径在仿真环境中的外观和性质。

具体来说，Smoothness 参数指定了路径中相邻路径点之间的曲率变化程度。当 Smoothness 参数设置较高时，路径会更加平滑，曲线的变化会更加渐变。而当 Smoothness 参数设置较低时，路径可能会更加锐利，曲线的变化会更加突然。

调整 Smoothness 参数可以影响路径的形状和运动特性，从而影响到机器人或其他物体沿着路径移动时的平滑性和稳定性。通常情况下，更高的 Smoothness 值会产生更自然、更平滑的路径，但可能会导致路径的长度增加或者运动速度减慢。

总之，Smoothness 参数允许用户根据实际需求调整路径的平滑程度，以达到最佳的仿真效果。

### Q: v-rep /Path中的Subdivisions数值是什么意思？

在 V-REP 中，路径（Path）对象的 Subdivisions 参数表示路径中每个路径段（Segment）之间的分割数。该参数影响路径在仿真环境中的精细程度和平滑度。

具体来说，Subdivisions 参数指定了路径中每个路径段的分割数，即路径被分成多少个部分。当 Subdivisions 参数设置较高时，路径将被更细地分割，曲线的变化将更加平滑。而当 Subdivisions 参数设置较低时，路径将被分割成较少的部分，曲线的变化可能会更加突然。

调整 Subdivisions 参数可以影响路径的形状和运动特性，从而影响到机器人或其他物体沿着路径移动时的运动轨迹的细节和精度。通常情况下，更高的 Subdivisions 值会产生更精细、更平滑的路径，但可能会增加计算负载和减慢仿真速度。

总之，Subdivisions 参数允许用户根据实际需求调整路径的精细程度，以达到最佳的仿真效果。

### Q: 介绍函数sim.readVisionSensor

`sim.readVisionSensor` 是 V-REP 中用于读取视觉传感器数据的函数。它可以用于模拟机器人或虚拟环境中的视觉感知。

**语法**：
```lua
number result, table data = sim.readVisionSensor(number sensorHandle)
```

**参数**：
- `sensorHandle`（数字）：视觉传感器的句柄（handle），表示要读取数据的视觉传感器。

**返回值**：
- `result`（数字）：操作结果，如果成功读取数据，则返回非负整数，表示数据有效性。如果失败，则返回负数。
- `data`（表格）：包含从传感器读取的数据的表格。数据的具体内容取决于传感器的类型和设置。

**说明**：
- 这个函数用于读取视觉传感器的数据，例如相机或激光雷达传感器。
- 如果成功读取数据，则返回值 `result` 将是非负整数，表示读取成功。此时，数据将包含在 `data` 中。
- 如果读取失败，返回值 `result` 将是负数，表示出现了错误或无法读取数据。

**示例**：
```lua
local result, data = sim.readVisionSensor(sensorHandle)
if result >= 0 then
    -- 读取到了有效的数据，可以使用 data 进行后续处理
    -- data 包含了从传感器读取的具体数据
else
    -- 读取失败，处理错误情况
end
```

使用 `sim.readVisionSensor` 函数，你可以在V-REP中读取视觉传感器（如相机、激光雷达等）的数据，并据此进行后续的处理和决策。

## Path Script

```lua
--lua

-- 通过 require 函数引入了 sim 模块和 path_customization 模块，用于后续的仿真操作和路径定制化。
sim = require'sim'
path = require('path_customization')

-- 定义了一个名为 path.shaping 的函数。该函数接受三个参数：path（路径对象）、pathIsClosed（路径是否封闭）、upVector（路径延伸的方向向量）。
function path.shaping(path, pathIsClosed, upVector)
    local section = {-0.02, 0.001, 0.02, 0.001} -- 表示路径横截面的数组 section
    local color = {0.3, 0.3, 0.3} -- 表示形状颜色的数组 color
    local options = 0
    if pathIsClosed then  -- 根据路径是否封闭的标志位 pathIsClosed，设置 options 变量。
        options = options | 4
    end
    -- 根据给定的路径、横截面、选项和方向向量生成一个沿着路径延伸的形状。生成的形状存储在 shape 变量中。
    local shape = sim.generateShapeFromPath(path, section, options, upVector)  
    sim.setShapeColor(shape, nil, sim.colorcomponent_ambient_diffuse, color) -- 为生成的形状设置颜色。
    
    return shape
end
```

sim.lua（1968行）和path_customization.lua（1309行）都在C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\lua中。两者都规模巨大，吾人直接复用算了。(2024年5月12日)

### Q: sim 模块是什么模块？

sim 模块是 V-REP（Virtual Robot Experimentation Platform）中的一个 Lua 模块，用于提供与仿真环境进行交互的功能。在 V-REP 中，Lua 脚本是一种常用的编程语言，用于控制和定制仿真场景中的各种元素。

sim 模块提供了一系列函数，允许 Lua 脚本与仿真场景中的物体、传感器、路径等进行交互。这些函数包括但不限于：

1. 控制物体的位置、姿态和运动状态。
2. 获取和设置物体的属性和参数。
3. 操作传感器，获取传感器数据。
4. 创建、管理和控制路径对象。
5. 与仿真环境中的其他元素进行通信和交互。

通过 sim 模块提供的功能，用户可以编写 Lua 脚本来实现各种自动化任务、控制算法和仿真场景的定制化。sim 模块是 V-REP 中非常重要的一部分，为用户提供了灵活、强大的编程接口，使其能够充分利用 V-REP 的功能和资源。

### Q: v-rep中的DefaultLight是什么？

在 V-REP（Virtual Robot Experimentation Platform）中，DefaultLight 是一个默认的光源对象，用于模拟场景中的光照效果。

DefaultLight 具有以下特点和功能：

1. **默认光源**：在创建新场景时，默认情况下会自动添加一个 DefaultLight 对象。这个光源会提供一定的光照效果，使得场景中的物体能够在仿真环境中可见。

2. **光照属性**：DefaultLight 具有各种光照属性，包括光照颜色、光照强度、光照范围等。用户可以根据需要调整这些属性，以获得所需的光照效果。

3. **影响物体**：DefaultLight 对象会影响场景中的物体的外观和可见性。通过调整光照属性，可以改变物体的明暗程度和投影效果，从而使得物体在仿真环境中呈现出不同的视觉效果。

总之，DefaultLight 是 V-REP 中用于模拟光照效果的默认光源对象，它在场景中起着重要的作用，可以影响到物体的外观和可见性，从而使得仿真环境更加真实和逼真。

```lua
--lua

function sysCall_init()
    -- 引入了 V-REP（Virtual Robot Experimentation Platform）中的 sim 和 simUI 模块，用于与仿真环境进行交互以及创建用户界面。
    sim = require('sim')
    simUI = require('simUI')
    -- 获取了当前脚本所属对象的句柄，通常是一个移动机器人对象。
    bubbleRobBase = sim.getObject('.')
    -- 分别获取了左电机、右电机和鼻子传感器对象的句柄。
    leftMotor = sim.getObject("./leftMotor")
    rightMotor = sim.getObject("./rightMotor")
    noseSensor = sim.getObject("./sensingNose")
    -- 定义了机器人的速度范围，单位为弧度每秒。
    minMaxSpeed = {50 * math.pi / 180,300 * math.pi / 180}
    -- 初始化了一个变量，用于记录机器人是否处于前进或后退模式。初始值为 -1，表示机器人处于前进模式。
    backUntilTime = -1 -- Tells whether bubbleRob is in forward or backward mode
    floorSensorHandles = {-1, -1, -1} -- 初始化了一个数组，用于存储地面传感器对象的句柄。
    -- 分别获取了左侧、中间和右侧地面传感器对象的句柄。
    floorSensorHandles[1] = sim.getObject("./leftSensor")
    floorSensorHandles[2] = sim.getObject("./middleSensor")
    floorSensorHandles[3] = sim.getObject("./rightSensor")
    robotTrace = sim.addDrawingObject(sim.drawing_linestrip + sim.drawing_cyclic, 2, 0, -1, 200, {1, 1, 0}, nil, nil, {1, 1, 0})  -- 创建了一个绘图对象，用于绘制机器人的移动轨迹。
    -- Create the custom UI:
    xml = '<ui title="'..sim.getObjectAlias(bubbleRobBase,1)..' speed" closeable="false" resizeable="false" activate="false">'..[[
                <hslider minimum="0" maximum="100" on-change="speedChange_callback" id="1"/>
            <label text="" style="* {margin-left: 300px;}"/>
        </ui>
        ]]
    -- 通过字符串拼接生成 XML 格式的 UI 描述，包含一个水平滑块和一个标签，用于控制和显示机器人的速度。然后使用 simUI.create(xml) 创建了该 UI。
    ui = simUI.create(xml)
    speed = (minMaxSpeed[1] + minMaxSpeed[2]) * 0.5 -- 计算了初始速度
    -- 设置了滑块的初始数值。
    simUI.setSliderValue(ui, 1, 100 * (speed - minMaxSpeed[1]) / (minMaxSpeed[2] - minMaxSpeed[1]))
end

-- 在仿真过程中对机器人的感知进行处理
function sysCall_sensing()
    local p = sim.getObjectPosition(bubbleRobBase) -- 通过 sim.getObjectPosition 函数获取了机器人的当前位置，并将其存储在变量 p 中。bubbleRobBase 是之前在 sysCall_init 函数中获取的机器人基本对象的句柄。
    sim.addDrawingObjectItem(robotTrace, p) -- 使用 sim.addDrawingObjectItem 函数将当前位置 p 添加到绘图对象 robotTrace 中。这样做可以实时绘制机器人的移动轨迹。
end 

function speedChange_callback(ui, id, newVal)
    -- 据新的滑块数值 newVal，计算了新的速度值 speed。
    speed = minMaxSpeed[1] + (minMaxSpeed[2] - minMaxSpeed[1]) * newVal / 100
end


-- 动作执行函数，用于在仿真过程中执行机器人的控制动作。
function sysCall_actuation() 
    -- 使用 sim.readProximitySensor 函数读取鼻子传感器的状态，返回值 result 表示检测到的障碍物距离。
    local result = sim.readProximitySensor(noseSensor)
    if result > 0 then -- 说明检测到了障碍物，将会执行后续的处理。
        backUntilTime = sim.getSimulationTime() + 4
    end
    
    -- read the line detection sensors:
    sensorReading = {false, false, false} -- 初始化了一个数组 sensorReading，用于存储三个对地面黑线传感器的检测结果
    for i = 1, 3, 1 do  -- 通过一个循环遍历三个地面传感器
        -- 使用 sim.readVisionSensor 函数读取地面传感器的状态
        local result, data = sim.readVisionSensor(floorSensorHandles[i])
        if result >= 0 then -- 传感器读取成功，将检测到的地面亮度数据存储在 data 中。
            -- 将对地面传感器的灰度数据与阈值 0.5 进行比较，如果灰度较低，则将相应位置的 sensorReading 设置为 true，表示检测到了路径黑线。
            sensorReading[i] = (data[11] < 0.5) -- data[11] is the average of intensity of the image
        end
    end
    
    -- 根据车上对地面传感器的检测结果，计算左右轮的速度，以跟随检测到的黑线。
    -- compute left and right velocities to follow the detected line:
    rightV = speed
    leftV = speed
    if sensorReading[1] then -- 如果检测到了左侧的黑线，将左轮速度设为 0.03 * speed，(左轮慢右轮快则左转)
        leftV = 0.03 * speed
    end
    if sensorReading[3] then -- 如果检测到了右侧的黑线，将右轮速度设为 0.03 * speed。(右轮慢左轮快则右转)
        rightV = 0.03 * speed
    end
    if sensorReading[1] and sensorReading[3] then -- 如果同时检测到左右两侧的黑线，将设置一个后退时间 backUntilTime，以便在后续的处理中执行后退动作。
        backUntilTime = sim.getSimulationTime() + 2
    end
    
    -- 根据当前时间和后退时间的比较，决定机器人是前进还是后退。
    if backUntilTime < sim.getSimulationTime() then -- 如果当前时间超过了后退时间，则执行前进动作；否则执行后退动作。
        -- When in forward mode, we simply move forward at the desired speed
        sim.setJointTargetVelocity(leftMotor, leftV)
        sim.setJointTargetVelocity(rightMotor, rightV)
    else
        -- When in backward mode, we simply backup in a curve at reduced speed
        sim.setJointTargetVelocity(leftMotor, -speed / 2)
        sim.setJointTargetVelocity(rightMotor, -speed / 8)
    end
end 

-- 仿真结束时被调用，用于清理资源和执行必要的清理操作。
function sysCall_cleanup() 
    simUI.destroy(ui) -- 用于销毁指定的用户界面（UI）对象，以释放相关资源。
end 
```

### Q: v-rep脚本中的main函数在哪？换言之，怎么知道脚本中函数的执行顺序？

在 V-REP 中，没有像传统编程语言中的 `main` 函数一样的入口函数。脚本中的函数执行顺序由事件触发和函数调用来确定。V-REP 使用了一种事件驱动的编程模型，其中不同的函数在特定的事件发生时被调用。

在 V-REP 脚本中，常见的事件包括 `sysCall_init`、`sysCall_sensing`、`sysCall_actuation`、`sysCall_cleanup` 等。这些事件对应着仿真过程中的不同阶段或行为。例如：

- `sysCall_init` 在仿真开始时被调用，用于初始化脚本中的变量和对象。
- `sysCall_sensing` 在感知阶段被调用，用于处理传感器数据。
- `sysCall_actuation` 在执行阶段被调用，用于执行控制动作。
- `sysCall_cleanup` 在仿真结束时被调用，用于清理资源。

除了这些系统事件外，用户还可以自定义其他事件，通过 `sim.setScriptAttribute` 函数设置触发条件，并在对应的函数中编写处理逻辑。

因此，在 V-REP 脚本中，函数的执行顺序由系统事件触发和函数调用来确定。要了解脚本中函数的执行顺序，需要了解 V-REP 的事件模型和相应的触发条件。

### Q: 什么是回调函数？

回调函数是一种常见的编程概念，指的是一个函数作为参数传递给另一个函数，并在特定条件满足时由后者调用。这种机制允许我们将一些特定的行为委托给另一个函数，在特定的情况下由后者执行。

回调函数通常用于以下场景：

1. **事件处理**：在事件发生时调用回调函数来处理事件，例如在用户点击按钮时执行某个动作。

2. **异步操作**：在异步操作完成时调用回调函数来处理结果，例如在文件下载完成后执行某个操作。

3. **定时器**：在定时器触发时调用回调函数来执行定时任务。

4. **状态通知**：在特定状态发生改变时调用回调函数来通知其他部分。

5. **用户交互**：在用户操作UI元素时调用回调函数来处理用户输入。

在回调函数中，通常会将某些参数传递给回调函数，以便在调用时使用。这样的参数可以是事件的状态、操作的结果等等。回调函数的使用使得代码更加模块化和灵活，能够适应不同的需求和情况。

### Q: 怎样修改v-rep中某个圆柱体的尺寸？

Mine: 双击圆柱体图标，选择Geometry即可修改。(2024年5月12日)

### Q: 为什么function path.shaping(path,pathIsClosed,upVector)   local section={0.02,-0.02,0.02,0.02,-0.02,0.02,-0.02,-0.02,0.02,-0.02}
时sensor无法探测到轨迹，改成function path.shaping(path, pathIsClosed, upVector)     local section = {-0.02, 0.001, 0.02, 0.001}
就可以探测到了？
CG: 在CoppeliaSim (旧名 V-REP) 中，使用路径形状（`path.shaping`）功能可以根据给定的轨迹和断面来创建一个实体物体。当你在仿真环境中使用传感器（比如接近传感器或激光传感器等）探测这些物体时，物体的几何形状和大小对于传感器的探测能力是非常关键的。

在你提供的两个例子中：

**第一个例子**：

```lua
local section={0.02,-0.02,0.02,0.02,-0.02,0.02,-0.02,-0.02,0.02,-0.02}
```

这里定义了一个相对复杂的断面形状，可能是一个较为复杂的多边形。根据CoppeliaSim中`path.shaping`函数的工作原理，这个断面会沿着给定路径生成面片，从而形成一个实体物体。如果这个断面形状或者由它生成的实体物体过于细小或者复杂，它可能因为传感器的分辨率限制而难以被探测到。

**第二个例子**：

```lua
local section = {-0.02, 0.001, 0.02, 0.001}
```

这里定义的是一个更简单、更扁平的断面形状，可能是一个简单的直线段或极薄的矩形。这种断面形状创建的物体边缘更加明显，形体更加扁平宽大，因而更容易被传感器探测到。

**为什么会有差异**：

1. **传感器的分辨率**：传感器对物体的探测能力受到其分辨率的限制。更细小或复杂的物体可能难以被准确探测。
   
2. **物体的几何特性**：较扁平宽大的物体提供了更大的“目标面积”给传感器探测，因此更容易被感知。

在进行仿真设计时，如果需要用传感器来探测由路径形状创建的实体物体，建议设计较为简单且具有一定体积的断面形状，以提高传感器的探测率。此外，也需要考虑优化传感器的配置（如感应范围、分辨率等）以适应场景中物体的特性。

### Q: CoppeliaSim有哪些方法可以设置设置Path中的ctrlPt？

在CoppeliaSim（前身为V-REP）中，路径（Path）由一系列控制点（ctrlPts）定义，这些控制点决定了路径的形状和走向。您可以通过以下几种方法设置或修改路径中的控制点：

1. 图形界面（GUI）

这是最直观的方法，适用于不需要动态改变路径的情况：

- 在CoppeliaSim中，选中您想要编辑的路径对象。
- 在对象的属性中，找到路径编辑相关的按钮，点击它可以进入路径编辑模式。
- 在路径编辑模式下，您可以直接通过鼠标点击来添加新的控制点，或者选中并移动现有的控制点来调整路径。

2. Lua脚本API

CoppeliaSim提供了丰富的API函数，允许您通过编写Lua脚本动态地管理和修改路径中的控制点：

- **sim.insertPathCtrlPoints**: 这个函数可以用来在路径中插入新的控制点。您可以指定插入位置、数量以及这些控制点的各项参数（位置、方向等）。
  
  例如，向路径添加一个新的控制点：
  ```lua
  sim.insertPathCtrlPoints(pathHandle, options, startIndex, ptCnt, ctrlPts)
  ```
  其中 `pathHandle` 是路径对象的句柄，`options` 用于指定操作选项（例如是否关联方向等），`startIndex` 指定从哪个位置开始插入，`ptCnt` 和 `ctrlPts` 分别指定要插入的控制点数量和具体参数。

- **sim.removePathCtrlPoints**: 这个函数可以移除路径中的控制点。
  
  例如，移除一部分控制点：
  ```lua
  sim.removePathCtrlPoints(pathHandle, startIndex, ptCnt)
  ```
  其中 `startIndex` 和 `ptCnt` 指定了要移除控制点的起始位置和数量。

- **sim.getPathCtrlPoints**: 这个函数可以获取路径中的控制点信息，允许您查询现有控制点的位置、方向等参数。

  获取路径的控制点信息：
  ```lua
  ctrlPoints = sim.getPathCtrlPoints(pathHandle, options)
  ```
  其中 `options` 用于指定操作选项。

3. CoppeliaSim的Remote API

如果您需要从外部程序（如Python脚本）中控制CoppeliaSim路径，可以通过CoppeliaSim的Remote API进行。Remote API允许外部程序通过网络与CoppeliaSim交互，但请注意，直接通过Remote API修改路径控制点的能力可能受到限制，具体取决于您使用的Remote API客户端库的功能。

通常，您可以通过Remote API执行Lua脚本命令来间接实现这种控制，如调用上述Lua API函数来添加、删除或获取路径控制点。

在使用这些方法时，请确保您熟悉CoppeliaSim的操作界面和Lua脚本编程。详细的API文档可以在CoppeliaSim官方网站或安装目录的文档中找到，它将提供更具体的函数使用方法和参数说明。

# movingAlongAPath-lua.ttt解读

```lua
--redCube lua

function sysCall_init()
    sim = require('sim')
    cube=sim.getObject('.') -- 获取当前脚本绑定对象(redCube)的句柄。
    path=sim.getObject('/Path') -- 获取场景中名为“Path”的路径对象的句柄。
    pathData=sim.unpackDoubleTable(sim.readCustomDataBlock(path,'PATH')) -- 读取路径对象自定义数据块中的“PATH”字段，并将其解压缩为一个双精度浮点数表（存储路径的控制点信息）。
    -- #pathData//7 计算了 pathData 数组的长度，并且除以 7，得到了矩阵的行数。
	--然后，7 被用作列数，因为每个数据元素代表路径中的一个点，每个点通常有 7 个相关联的数值（如 x、y、z 坐标以及姿态等）。
    local m=Matrix(#pathData//7,7,pathData)
    pathPositions=m:slice(1,1,m:rows(),3):data()  -- 位置
    pathQuaternions=m:slice(1,4,m:rows(),7):data() -- 旋转
    pathLengths,totalLength=sim.getPathLengths(pathPositions,3) -- 每段路径的长度和总长度
    velocity=0.05 -- m/s
    posAlongPath=0 -- 对象当前沿路径的位置
    previousSimulationTime=0
end

function sysCall_actuation()
    local t=sim.getSimulationTime() -- 获取当前仿真时间（以秒为单位）。CoppeliaSim的仿真环境根据设置的仿真步长来推进时间，获取当前时间是计算移动距离的基础。
    posAlongPath=posAlongPath+velocity*(t-previousSimulationTime) -- 表示对象在路径上的位置。通过计算自上一仿真步骤以来经过的时间并乘以速度(velocity)，可以得出对象在路径上应该移动的距离，并加到当前位置上。
    posAlongPath=posAlongPath % totalLength -- 确保posAlongPath在到达路径末尾时能够循环回到开始，通过取余totalLength（路径的总长度），实现路径循环。
    local pos=sim.getPathInterpolatedConfig(pathPositions,pathLengths,posAlongPath) -- 调用sim.getPathInterpolatedConfig函数，根据当前位置(posAlongPath)在路径上获得插值后的位置坐标。这个函数会考虑路径的形状和对象应在的确切位置，计算得出准确的三维空间坐标。
    local quat=sim.getPathInterpolatedConfig(pathQuaternions,pathLengths,posAlongPath,nil,{2,2,2,2}) -- 获取对象在当前位置(posAlongPath)的四元数表示的旋转状态。传递额外的参数{2,2,2,2}用于指定插值方法，特别是对于四元数这样的旋转数据。
    sim.setObjectPosition(cube,pos,path) -- 根据计算得到的位置(pos)更新对象（在这个例子中是cube）的位置
    sim.setObjectQuaternion(cube,quat,path) -- 计算得到的四元数(quat)更新对象的旋转状态。
    previousSimulationTime=t -- 更新previousSimulationTime为当前仿真时间，为下一仿真步骤的计算准备。
end
```

在上述代码中，位置不是通过速度仿真得到的，而是通过计算得到的。(2024年5月13日) => 试试加上碰撞检测？

```lua
--blueCube lua

function sysCall_init()
    sim = require('sim')
    cube=sim.getObject('.') -- 获取当前脚本绑定对象(redCube)的句柄。
    path=sim.getObject('/Path') -- 获取场景中名为“Path”的路径对象的句柄。
    pathData=sim.unpackDoubleTable(sim.readCustomDataBlock(path,'PATH')) -- 读取路径对象自定义数据块中的“PATH”字段，并将其解压缩为一个双精度浮点数表（存储路径的控制点信息）。
    -- #pathData//7 计算了 pathData 数组的长度，并且除以 7，得到了矩阵的行数。
	--然后，7 被用作列数，因为每个数据元素代表路径中的一个点，每个点通常有 7 个相关联的数值（如 x、y、z 坐标以及姿态等）。
    local m=Matrix(#pathData//7,7,pathData)
    pathPositions=m:slice(1,1,m:rows(),3):data() -- 位置
    pathQuaternions=m:slice(1,4,m:rows(),7):data()
    pathLengths,totalLength=sim.getPathLengths(pathPositions,3) -- 每段路径的长度和总长度
    velocity=0.04 -- m/s
    posAlongPath=0 -- 对象当前沿路径的位置
    previousSimulationTime=0
    sim.setStepping(true) -- 仿真不会连续运行，而是在每个仿真步骤后暂停，等待用户手动使仿真前进到下一个步骤
end

function sysCall_thread() -- 定义的线程函数，它在线程的生命周期内不断地循环直至线程结束或仿真停止。
    while true do
        local t=sim.getSimulationTime() -- 获取当前仿真时间（以秒为单位）。CoppeliaSim的仿真环境根据设置的仿真步长来推进时间，获取当前时间是计算移动距离的基础。
        posAlongPath=posAlongPath+velocity*(t-previousSimulationTime) -- 表示对象在路径上的位置。通过计算自上一仿真步骤以来经过的时间并乘以速度(velocity)，可以得出对象在路径上应该移动的距离，并加到当前位置上。
        posAlongPath=posAlongPath % totalLength -- 确保posAlongPath在到达路径末尾时能够循环回到开始，通过取余totalLength（路径的总长度），实现路径循环。
        local pos=sim.getPathInterpolatedConfig(pathPositions,pathLengths,posAlongPath) -- 调用sim.getPathInterpolatedConfig函数，根据当前位置(posAlongPath)在路径上获得插值后的位置坐标。这个函数会考虑路径的形状和对象应在的确切位置，计算得出准确的三维空间坐标。
        local quat=sim.getPathInterpolatedConfig(pathQuaternions,pathLengths,posAlongPath,nil,{2,2,2,2}) -- 获取对象在当前位置(posAlongPath)的四元数表示的旋转状态。传递额外的参数{2,2,2,2}用于指定插值方法，特别是对于四元数这样的旋转数据。
        sim.setObjectPosition(cube,pos,path) -- 根据计算得到的位置(pos)更新对象（在这个例子中是cube）的位置
        sim.setObjectQuaternion(cube,quat,path) -- 计算得到的四元数(quat)更新对象的旋转状态。
        previousSimulationTime=t -- 更新previousSimulationTime为当前仿真时间，为下一仿真步骤的计算准备。
        sim.step()
    end
end
```

### Q: 下面函数中，sim.setStepping(true)是什么意思？

在CoppeliaSim中，`sim.setStepping(true)`调用是用来开启或激活“步进模式”（Stepping mode）。在步进模式下，仿真不会连续运行，而是在每个仿真步骤后暂停，等待用户手动使仿真前进到下一个步骤。这个模式对于调试和教学目的特别有用，因为它允许用户仔细观察和分析仿真的每个阶段，理解仿真模型的行为。

`sim.setStepping(true)`调用使得步进模式被激活，意味着仿真将在每次仿真步骤后暂停。这对于逐步执行仿真、检查变量状态、或者更精细地控制仿真流程非常有帮助。开启步进模式后，通常需要通过CoppeliaSim的用户界面中的相应按钮或通过脚本调用来手动前进仿真。

在脚本开头调用`sim.setStepping(true)`意味着从仿真开始就启用这种模式，确保了仿真的每个步骤都能被精确地控制和观察。这可以是对某些特定仿真场景的需求，特别是在进行复杂场景的调试或教育演示时，步进模式显示出其价值。

总结来说，`sim.setStepping(true)`在您的脚本中用于控制仿真的执行方式，允许逐步执行仿真来更好地观察和理解模型的动态行为。

### Q: sim.step() ?

sim.step() 的调用是该脚本与其他简单循环脚本的主要区别，它允许在线程内手动控制仿真的每一步。这种方式使得脚本可以在每个仿真“步”中执行复杂的逻辑处理，而不是依赖CoppeliaSim的自动时间流逝。它特别有用于创建精准的控制逻辑或实时仿真接口。

### Q: red cube用的sysCall_actuation()，blue cube用的sysCall_thread()，两者有什么区别？

在CoppeliaSim（以前称为V-REP）的脚本环境中，`sysCall_actuation()`和`sysCall_thread()`是两种不同类型的回调函数，它们在仿真过程中起着不同的作用。理解这两者之间的区别有助于更合理和有效地编写仿真脚本。

`sysCall_actuation()`:

- **周期性回调**：`sysCall_actuation()`是一个在每个仿真步的“行动（actuation）”阶段被调用的周期性回调函数。这意味着在仿真的每个时间步骤内，系统会自动调用这个函数，使其成为实现物体行动逻辑的理想场所，如移动部件、应用力和扭矩等。
- **自动同步**：由于`sysCall_actuation()`在仿真的固定周期内被触发，它与仿真环境自动同步，无需用户手动控制时间步进。这在大多数情况下简化了脚本的编写。

`sysCall_thread()`:

- **独立线程**：`sysCall_thread()`在一个独立的线程中执行。这意味着它可以实现持续运行的复杂逻辑而不影响其他脚本的执行。线程可以空闲运行，也可以通过`sim.switchThread()`主动让出控制权，或通过`sim.step()`在需要时手动推进仿真时间步骤。
- **手动同步**：在`sysCall_thread()`中，如果使用`sim.step()`，则脚本需要自行管理时间步进和同步。这提供了更大的灵活性，但也需要开发者对时间控制有更精确的理解和操作，以避免创建时间管理错误。

**使用场景比较：**

- **`sysCall_actuation()`的使用场景**：当你需要在每个仿真步执行简单或周期性的任务时，如更新驱动对象的位置或计算物理量，`sysCall_actuation()`非常合适。这简化了脚本的同步与仿真流程。
  
- **`sysCall_thread()`的使用场景**：当任务需要独立于主仿真循环长时间运行，或者需要复杂的条件逻辑、循环和等待（无需阻塞主仿真循环）时，使用`sysCall_thread()`更合适。它为开发者提供了线程控制的灵活性，适用于需要复杂逻辑和时间管理的场景。

**结论：**

选择`sysCall_actuation()`还是`sysCall_thread()`依赖于你具体的需求和任务复杂度。如果任务与仿真的每个时间步骤紧密相关并且需要紧跟仿真的进程，使用`sysCall_actuation()`更简单直接。如果任务更加独立或需要灵活的时间管理和复杂逻辑，`sysCall_thread()`可能是更好的选择。在`sysCall_thread()`中，手动管理仿真的时间步骤可以提供额外的控制，但也增加了脚本复杂性和出错的风险。

```lua
-- Child script /Path lua

function sysCall_init()
    sim = require('sim')
    path=sim.getObject('.') -- 获取当前脚本绑定对象(redCube)的句柄。
    pathData=sim.unpackDoubleTable(sim.readCustomDataBlock(path,'PATH')) -- 读取路径对象自定义数据块中的“PATH”字段，并将其解压缩为一个双精度浮点数表（存储路径的控制点信息）。
    -- #pathData//7 计算了 pathData 数组的长度，并且除以 7，得到了矩阵的行数。
	--然后，7 被用作列数，因为每个数据元素代表路径中的一个点，每个点通常有 7 个相关联的数值（如 x、y、z 坐标以及姿态等）。
    local m=Matrix(math.floor(#pathData/7),7,pathData) 
    pathPositions=m:slice(1,1,m:rows(),3):data() -- 位置
    pathQuaternions=m:slice(1,4,m:rows(),7):data() -- 旋转
    local cubeCount=100
    -- 在路径上计划放置100个blackCube对象。第一个对象是直接通过名字/blackCube从场景中获得，后续的对象则是通过复制粘贴第一个对象来创建的。
    cube=sim.getObject('/blackCube') -- 第一个对象是直接通过名字/blackCube从场景中获得
    objectsToMove={cube}
    for i=2,cubeCount,1 do
        objectsToMove[i]=sim.copyPasteObjects({cube},0)[1] -- 后续的对象则是通过复制粘贴第一个对象来创建的。
    end
    for i=1,cubeCount,1 do
        sim.setObjectParent(objectsToMove[i],path,true) -- not required, but looks cleaner
    end
    
    pathLengths,totalLength=sim.getPathLengths(pathPositions,3) -- 基于提取的位置数据计算路径的长度，以及从起点到每个控制点的长度列表pathLengths和路径的总长度totalLength。
    offset=totalLength/#objectsToMove -- 计算沿路径分布对象的间隔距离，使这些对象均匀地分布在路径上。
    v=0.06 -- 设定对象沿路径移动的速度。
    sim.setStepping(true) -- 仿真不会连续运行，而是在每个仿真步骤后暂停，等待用户手动使仿真前进到下一个步骤
end

function sysCall_thread() -- 创建一个新的线程。该线程会在模拟运行时独立于主线程运行
    while true do
        setPathPosition(sim.getSimulationTime()*v)
        sim.step() -- 执行一次模拟步进，使模拟时间向前推进一个固定的时间步长。
    end
end

function setPathPosition(p)
    for i=1,#objectsToMove,1 do
        p=p % totalLength -- 确保了p的值总是在路径的总长度范围内。
        local h=objectsToMove[i]
        local pos=sim.getPathInterpolatedConfig(pathPositions,pathLengths,p)
        local quat=sim.getPathInterpolatedConfig(pathQuaternions,pathLengths,p,nil,{2,2,2,2})
        sim.setObjectPosition(h,pos,path) -- 对象h在场景中相对于路径的位置
        sim.setObjectQuaternion(h,quat,path) -- 对象h在场景中相对于路径的旋转方向
        p=p+offset
    end
end
```

### Q: v-rep中的collidable, measurable, detectable分别是什么意思？

在V-REP中，这些术语描述了物体的属性和行为：

1. **Collidable（可碰撞的）：** 指示物体是否可以参与碰撞检测。如果物体被标记为可碰撞的，则它会与其他可碰撞物体进行碰撞检测。通常，这适用于实体物体，如机器人、墙壁、家具等。

2. **Measurable（可测量的）：** 表示物体是否具有可测量的特征，如体积、质量、惯性等。如果物体被标记为可测量的，则可以使用传感器或其他设备对其进行测量和监测。

3. **Detectable（可检测的）：** 表示物体是否可以被传感器或其他检测设备检测到。如果物体被标记为可检测的，则可以使用传感器或视觉系统等设备检测其存在、位置、状态等信息。

这些属性可以单独或同时应用于物体，具体取决于物体在场景中的角色和行为。例如，一个机器人可能会被标记为可碰撞的、可测量的和可检测的，以便与其他物体进行碰撞检测、测量其位置和姿态，并使用传感器检测其周围环境。

### Q: 怎样给v-rep中添加碰撞检测器？

在CoppeliaSim（以前称为V-REP）中添加碰撞检测器可以通过图形界面和脚本进行。以下是两种方法的步骤：

**方法一：使用图形界面添加碰撞检测器**

1. **启动CoppeliaSim并加载场景**：
   打开CoppeliaSim并加载或创建一个场景。

2. **选择物体**：
   在场景中选择你想要进行碰撞检测的物体。你可以在场景层次结构中点击选择物体。

3. **添加碰撞检测器**：
   - 在菜单栏中，选择 **“工具” -> “碰撞检测”**。
   - 在弹出的碰撞检测对话框中，点击 **“添加新碰撞检测对象”**。
   - 选择你想要进行碰撞检测的两个物体（或一个物体和环境），然后点击 **“确定”**。

4. **设置碰撞检测属性**：
   - 在碰撞检测对话框中，你可以看到新添加的碰撞检测对象。
   - 设置所需的属性，例如启用或禁用碰撞检测，设置碰撞检测的处理频率等。

5. **运行模拟**：
   - 运行模拟，CoppeliaSim会自动进行碰撞检测，并在检测到碰撞时更新碰撞状态。

**方法二：使用Lua脚本添加碰撞检测器**

1. **启动CoppeliaSim并加载场景**：
   打开CoppeliaSim并加载或创建一个场景。

2. **创建或编辑脚本**：
   - 在场景层次结构中选择一个对象（例如，一个机器人或传感器）。
   - 在属性对话框中，点击 **“附加子脚本”**，然后选择 **“非线程子脚本”** 或 **“线程子脚本”**。

3. **编写脚本代码**：
   在脚本编辑器中，添加以下Lua代码来创建和管理碰撞检测器：

   ```lua
   function sysCall_init()
       -- 获取两个要检测碰撞的对象的句柄
       objectHandle1 = sim.getObjectHandle('ObjectName1')
       objectHandle2 = sim.getObjectHandle('ObjectName2')
       
       -- 创建碰撞检测器
       collisionHandle = sim.addCollision(objectHandle1, objectHandle2)
   end
   
   function sysCall_sensing()
       -- 检查碰撞
       collisionState = sim.readCollision(collisionHandle)
       if collisionState > 0 then
           -- 如果检测到碰撞，执行相应的操作
           print('Collision detected between ObjectName1 and ObjectName2')
       end
   end
   ```

4. **运行模拟**：
   - 运行模拟，CoppeliaSim会自动进行碰撞检测，并在检测到碰撞时执行脚本中的操作。

**总结**

通过以上两种方法，可以在CoppeliaSim中添加和管理碰撞检测器。使用图形界面的方法适合快速设置和可视化调试，而使用脚本的方法适合复杂的逻辑控制和动态管理。选择适合你的具体需求的方法来进行碰撞检测设置。

```lua
-- Joint lua

function sysCall_init()
    sim = require('sim')
    joint=sim.getObject('.')
end

function sysCall_actuation()
    sim.setJointPosition(joint,sim.getJointPosition(joint)+0.01)
end
```

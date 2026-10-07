# -*- coding: utf-8 -*-
# 生成 RemoteCompanionCN.x —— 映射表全部 \uXXXX 转义为纯 ASCII（Triggr 教训）
import re

EXACT = {
 "ACTION SEQUENCE": "动作序列",
 "Access Token": "访问令牌",
 "Action Options": "动作选项",
 "Actions": "动作",
 "Add Delay": "添加延迟",
 "Add Else If": "添加否则如果",
 "Add Else": "添加否则",
 "Add Nested If": "添加嵌套如果",
 "Add": "添加",
 "App Launch": "应用启动",
 "App": "应用",
 "Are you sure you want to clear all actions from this trigger?": "确定要清除此触发器的全部动作吗？",
 "Bluetooth Device": "蓝牙设备",
 "Broker Host": "服务器主机",
 "Cancel": "取消",
 "Change Macro…": "更改宏…",
 "Choose a status to evaluate": "选择要判断的状态",
 "Clear All Actions": "清除全部动作",
 "Clear": "清除",
 "Client ID": "客户端 ID",
 "Configuration file has been saved.": "配置文件已保存。",
 "Configuration restored. Return to Triggers to see changes.": "配置已恢复。返回触发器页查看更改。",
 "Connected to Device": "已连接设备",
 "Connected to Home Assistant successfully!": "已成功连接 Home Assistant！",
 "Connected to Keyboard Maestro Web Server successfully!": "已成功连接 Keyboard Maestro Web 服务器！",
 "Connected to Network": "已连接网络",
 "Connecting to Home Assistant...": "正在连接 Home Assistant…",
 "Connecting to Keyboard Maestro Web Server...": "正在连接 Keyboard Maestro Web 服务器…",
 "Connecting to MQTT Broker...": "正在连接 MQTT 服务器…",
 "Connection Failed": "连接失败",
 "Connection Successful": "连接成功",
 "Copied to Clipboard": "已复制到剪贴板",
 "Copied!": "已复制！",
 "Copy Path": "复制路径",
 "Copy Settings": "复制设置",
 "Copy": "复制",
 "Could not connect to MQTT broker": "无法连接 MQTT 服务器",
 "Could not export configuration": "无法导出配置",
 "Custom Swipe": "自定义滑动",
 "Day Required": "必须选择日期",
 "Debug Log": "调试日志",
 "Default Topic Prefix": "默认主题前缀",
 "Delete Block": "删除代码块",
 "Delete Else If": "删除否则如果",
 "Delete": "删除",
 "Device Locked": "设备已锁定",
 "Device Unlocked": "设备已解锁",
 "Disabled": "已停用",
 "Disconnected from Device": "已断开设备",
 "Disconnected from Network": "已断开网络",
 "Edit Action": "编辑动作",
 "Edit Condition": "编辑条件",
 "Edit Delay": "编辑延迟",
 "Edit Parameter / Value…": "编辑参数/值…",
 "Enable All Triggers": "启用全部触发器",
 "Enable Home Assistant": "启用 Home Assistant",
 "Enable Keyboard Maestro": "启用 Keyboard Maestro",
 "Enable MQTT": "启用 MQTT",
 "Enabled (Default URL)": "已启用（默认 URL）",
 "Enabled (URL not configured)": "已启用（URL 未配置）",
 "End Time (e.g. 17:00)": "结束时间（如 17:00）",
 "Ensure AirPlay devices are reachable.": "请确保 AirPlay 设备可达。",
 "Ensure Bluetooth devices are paired.": "请确保蓝牙设备已配对。",
 "Enter Home Assistant command or entity ID (e.g. toggle light.bedroom or call light.turn_on light.bedroom):": "输入 Home Assistant 命令或实体 ID（如 toggle light.bedroom 或 call light.turn_on light.bedroom）：",
 "Enter IP address or hostname of your MQTT broker:": "输入 MQTT 服务器 IP 或主机名：",
 "Enter Macro Name or UUID (and optional trigger value):": "输入宏名称或 UUID（可附带触发值）：",
 "Enter SSID": "输入 SSID",
 "Enter a new name for this NFC tag:": "输入此 NFC 标签的新名称：",
 "Enter a value (0-100)": "输入数值（0-100）",
 "Enter default topic prefix for published events:": "输入事件发布的默认主题前缀：",
 "Enter delay in seconds": "输入延迟秒数",
 "Enter exact device name": "输入确切设备名",
 "Enter optional broker password:": "输入服务器密码（可选）：",
 "Enter optional broker username:": "输入服务器用户名（可选）：",
 "Enter optional trigger parameter/value passed to KM %TriggerValue%:": "输入传给 KM %TriggerValue% 的触发参数/值（可选）：",
 "Enter start and end time (e.g. 09:00 - 17:00 or 9:00 AM - 5:00 PM):": "输入开始与结束时间（如 09:00 - 17:00）：",
 "Enter terminal command (runs as root)": "输入终端命令（以 root 运行）",
 "Enter the MQTT topic and payload to publish:": "输入要发布的 MQTT 主题与内容：",
 "Enter the Web Server URL from Keyboard Maestro Preferences (e.g. http://192.168.1.50:4490 or https://192.168.1.30:4491):": "输入 Keyboard Maestro 偏好设置中的 Web 服务器 URL（如 http://192.168.1.50:4490）：",
 "Enter the full base URL of your Home Assistant instance:": "输入 Home Assistant 的完整基础 URL：",
 "Enter the optional password configured in Keyboard Maestro Web Server preferences:": "输入 Keyboard Maestro Web 服务器偏好中设置的密码（可选）：",
 "Enter the optional username configured in Keyboard Maestro Web Server preferences:": "输入 Keyboard Maestro Web 服务器偏好中设置的用户名（可选）：",
 "Enter the port number of your MQTT broker (default: 1883):": "输入 MQTT 服务器端口（默认 1883）：",
 "Enter toast title, subtitle and SFSymbol name": "输入弹窗标题、副标题和 SFSymbol 名称",
 "Enter unique client identifier for this device:": "输入本设备唯一的客户端标识：",
 "Enter value passed to KM %TriggerValue% (leave empty for none):": "输入传给 KM %TriggerValue% 的值（留空为无）：",
 "Error": "错误",
 "Execute as Root": "以 Root 执行",
 "Export Configuration": "导出配置",
 "Export Error": "导出错误",
 "Export Failed": "导出失败",
 "Export Successful": "导出成功",
 "Failed to Load Entities": "加载实体失败",
 "Failed to Load Macros": "加载宏失败",
 "Failed to fetch devices": "获取设备失败",
 "Favorite": "收藏",
 "Fetching paired devices...": "正在获取已配对设备…",
 "HTTP 401: Unauthorized (Check Username / Password)": "HTTP 401：未授权（检查用户名/密码）",
 "Home Assistant Command": "Home Assistant 命令",
 "Home Assistant Not Configured": "Home Assistant 未配置",
 "Home Assistant URL": "Home Assistant URL",
 "Home Assistant": "Home Assistant",
 "Import Actions": "导入动作",
 "Import Configuration": "导入配置",
 "Import Failed": "导入失败",
 "Import Successful": "导入成功",
 "Import": "导入",
 "Integrations": "集成服务",
 "Invalid configuration file": "配置文件无效",
 "Keyboard Maestro Macro": "Keyboard Maestro 宏",
 "Keyboard Maestro Not Configured": "Keyboard Maestro 未配置",
 "Keyboard Maestro Password": "Keyboard Maestro 密码",
 "Keyboard Maestro Server URL": "Keyboard Maestro 服务器 URL",
 "Keyboard Maestro Username": "Keyboard Maestro 用户名",
 "Keyboard Maestro": "Keyboard Maestro",
 "Keyword to match": "要匹配的关键词",
 "Leave empty for any payload, or e.g. ON": "留空匹配任意内容，或如 ON",
 "Loading...": "加载中…",
 "Long-Lived Access Token": "长期访问令牌",
 "MQTT Broker Host": "MQTT 服务器主机",
 "MQTT Client ID": "MQTT 客户端 ID",
 "MQTT Password": "MQTT 密码",
 "MQTT Port": "MQTT 端口",
 "MQTT Topic": "MQTT 主题",
 "MQTT Username": "MQTT 用户名",
 "MQTT": "MQTT",
 "MQTT: Publish Topic": "MQTT：发布主题",
 "Macro Name or UUID (e.g. Sleep Display)": "宏名称或 UUID（如 Sleep Display）",
 "Macro": "宏",
 "Manual Entry": "手动输入",
 "Media Paused": "媒体已暂停",
 "Media Playing": "媒体播放中",
 "Media Track Changed": "媒体曲目切换",
 "Missing Configuration": "缺少配置",
 "Missing Topic": "缺少主题",
 "Modify the command": "修改命令",
 "My Device": "我的设备",
 "My Tag": "我的标签",
 "NFC Error": "NFC 错误",
 "NFC Not Supported": "不支持 NFC",
 "NFC Scanning": "NFC 扫描中",
 "NFC Tag": "NFC 标签",
 "Name Required": "必须填写名称",
 "New Trigger": "新建触发器",
 "No Actions": "无动作",
 "No Devices Found": "未找到设备",
 "No Paired Devices Found": "未找到已配对设备",
 "No actions configured for this trigger. Tap to add actions first.": "此触发器尚未配置动作，请先点按添加动作。",
 "No parameter configured": "未配置参数",
 "No valid actions found.": "未找到有效动作。",
 "Not Configured": "未配置",
 "Not configured": "未配置",
 "Notification": "通知",
 "OK": "好",
 "Optional": "可选",
 "Parameter / Value (optional)": "参数/值（可选）",
 "Password": "密码",
 "Paste Above": "粘贴到上方",
 "Paste Below": "粘贴到下方",
 "Paste the access token generated from your Home Assistant profile:": "粘贴 Home Assistant 个人资料页生成的访问令牌：",
 "Paste": "粘贴",
 "Payload (e.g. ON, TOGGLE, 1, or JSON)": "内容（如 ON、TOGGLE、1 或 JSON）",
 "Please configure Broker Host first.": "请先配置服务器主机。",
 "Please configure Keyboard Maestro Web Server URL first.": "请先配置 Keyboard Maestro Web 服务器 URL。",
 "Please configure Server URL and Access Token first.": "请先配置服务器 URL 和访问令牌。",
 "Please configure your Home Assistant Server URL and Access Token in Settings.": "请在设置中配置 Home Assistant 服务器 URL 和访问令牌。",
 "Please configure your Keyboard Maestro Web Server URL in Settings.": "请在设置中配置 Keyboard Maestro Web 服务器 URL。",
 "Please enter a WiFi network name.": "请输入 WiFi 网络名称。",
 "Please enter an MQTT topic to subscribe to.": "请输入要订阅的 MQTT 主题。",
 "Please install SpringCuts from Havoc to enable shortcuts support.": "请从 Havoc 源安装 SpringCuts 以启用快捷指令支持。",
 "Please select at least one day.": "请至少选择一天。",
 "Please wait": "请稍候",
 "Port": "端口",
 "Power Connected": "已接通电源",
 "Power Disconnected": "电源已断开",
 "Ready to Scan (NDEF Mode)...": "准备扫描（NDEF 模式）…",
 "Ready to Scan (Tag Mode)...": "准备扫描（标签模式）…",
 "Ready to Scan": "准备扫描",
 "Record Tap": "录制点击",
 "Remove Else": "移除否则",
 "Remove Parameter": "移除参数",
 "Rename Tag": "重命名标签",
 "Retry": "重试",
 "Root Command": "Root 命令",
 "SFSymbol name (optional, e.g. info.circle)": "SFSymbol 名称（可选，如 info.circle）",
 "Save": "保存",
 "Scan Cancelled": "扫描已取消",
 "Scan NFC Tag": "扫描 NFC 标签",
 "Scanning for devices...": "正在扫描设备…",
 "Scheduled Trigger": "定时触发器",
 "Search Actions": "搜索动作",
 "Search Apps": "搜索应用",
 "Search Entities": "搜索实体",
 "Search Macros & Groups": "搜索宏与分组",
 "Search Shortcuts": "搜索快捷指令",
 "Select Action": "选择动作",
 "Select AirPlay Device": "选择 AirPlay 设备",
 "Select App": "选择应用",
 "Select Bluetooth Device": "选择蓝牙设备",
 "Select Shortcut": "选择快捷指令",
 "Select a system event to trigger actions.": "选择一个用于触发动作的系统事件。",
 "Select a trigger type to expand your RemoteCompanion setup.": "选择触发器类型以扩展你的 RemoteCompanion 设置。",
 "Select desired mode/lens": "选择所需模式/镜头",
 "Select desired state": "选择所需状态",
 "Server URL": "服务器 URL",
 "Set": "设定",
 "Settings": "设置",
 "SpringCuts Missing": "缺少 SpringCuts",
 "Start Time (e.g. 09:00)": "开始时间（如 09:00）",
 "Subtitle (optional)": "副标题（可选）",
 "System Event": "系统事件",
 "Test Connection": "测试连接",
 "Test Macro": "测试宏",
 "Testing Connection...": "正在测试连接…",
 "There are no actions in this sequence to export.": "此序列没有可导出的动作。",
 "This device does not support NFC reading.": "此设备不支持 NFC 读取。",
 "Time of Day Condition": "时段条件",
 "Title (required)": "标题（必填）",
 "Toast": "弹窗",
 "Topic (e.g. home/livingroom/light/set)": "主题（如 home/livingroom/light/set）",
 "Topic Prefix": "主题前缀",
 "Trigger (No Parameter)": "触发（无参数）",
 "Trigger Value / Parameter (optional)": "触发值/参数（可选）",
 "Trigger with Parameter…": "带参数触发…",
 "UI Tweaker": "界面调整器",
 "Unfavorite": "取消收藏",
 "Update AirPlay Device": "更新 AirPlay 设备",
 "Update delay in seconds": "更新延迟秒数",
 "Update": "更新",
 "Username": "用户名",
 "Web Server URL": "Web 服务器 URL",
 "Web UI": "网页控制台",
 "WiFi Network": "WiFi 网络",
 "e.g. Inbound Alert": "如 Inbound Alert",
 "e.g. com.apple.ShazamNotifications": "如 com.apple.ShazamNotifications",
 "e.g. remotecompanion/cmd/ring": "如 remotecompanion/cmd/ring",
 "x y  (e.g. 195 422)": "x y（如 195 422）",
 "x y ms  (e.g. 195 422 800)": "x y 毫秒（如 195 422 800）",
 "x1 y1 x2 y2  (e.g. 195 700 195 200)": "x1 y1 x2 y2（如 195 700 195 200）",
 "192.168.1.50 or broker.local": "如 192.168.1.50 或 broker.local",
 "Keyword to match": "要匹配的关键词",
}

# 动态串：渲染后按正则匹配翻译（{0}{1} 为捕获组占位）
REGEX = [
 (r"^Connected to MQTT broker \((.+):(\d+)\) successfully!$", "已连接 MQTT 服务器（{0}:{1}）！"),
 (r"^Server returned HTTP status (\d+)$", "服务器返回 HTTP 状态 {0}"),
 (r"^Loaded (\d+) action\(s\)\.$", "已加载 {0} 个动作。"),
 (r"^Wait ([0-9.]+)s$", "等待 {0} 秒"),
 (r"^Delay ([0-9.]+)s$", "延迟 {0} 秒"),
 (r"^Toggle \((.+)\)$", "切换（{0}）"),
 (r"^Turn On \((.+)\)$", "打开（{0}）"),
 (r"^Turn Off \((.+)\)$", "关闭（{0}）"),
 (r"^Parameter: (.+)$", "参数：{0}"),
 (r"^Trigger: (.+)$", "触发器：{0}"),
 (r"^Any Notification from (.+)$", "来自 {0} 的任意通知"),
 (r"^Any Notification containing '(.+)'$", "包含「{0}」的任意通知"),
 (r"^Notification from (.+) containing '(.+)'$", "来自 {0} 且包含「{1}」的通知"),
 (r"^Connect (.+)$", "连接 {0}"),
 (r"^Disconnect (.+)$", "断开 {0}"),
 (r"^Kill (.+)$", "结束 {0}"),
 (r"^Launch (.+)$", "启动 {0}"),
 (r"^Open (.+)$", "打开 {0}"),
 (r"^Run (.+)$", "运行 {0}"),
 (r"^Swipe (.+)$", "滑动 {0}"),
 (r"^Hold at (.+)$", "长按 {0}"),
 (r"^Tap at (.+)$", "点击 {0}"),
 (r"^Repeat (.+)$", "重复 {0}"),
 (r"^Set Brightness (.+)$", "设置亮度 {0}"),
 (r"^Set Volume (.+)$", "设置音量 {0}"),
 (r"^Flashlight ([0-9.]+)%$", "手电筒 {0}%"),
 (r"^HA Toggle: (.+)$", "HA 切换：{0}"),
 (r"^HA Turn On: (.+)$", "HA 打开：{0}"),
 (r"^HA Turn Off: (.+)$", "HA 关闭：{0}"),
 (r"^HA Call (.+)$", "HA 调用 {0}"),
 (r"^HA: (.+)$", "HA：{0}"),
 (r"^KM: (.+) \((.+)\)$", "KM：{0}（{1}）"),
 (r"^KM: (.+)$", "KM：{0}"),
 (r"^MQTT: (.+) \((.+)\)$", "MQTT：{0}（{1}）"),
 (r"^MQTT: (.+)$", "MQTT：{0}"),
 (r"^NFC Tag (.+)$", "NFC 标签 {0}"),
 (r"^Error \(NDEF\): (.+)$", "错误（NDEF）：{0}"),
 (r"^Could not read file: (.+)$", "无法读取文件：{0}"),
 (r"^Found: (.+)$", "找到：{0}"),
 (r"^Open Camera \((.+)\)$", "打开相机（{0}）"),
 (r"^(.+) Time is Between (.+)$", "{0} 时间介于 {1}"),
 (r"^(.+) seconds$", "{0} 秒"),
 (r"^(.+) is\.\.\.$", "{0} 是…"),
 (r"^Could not connect to (.+)$", "无法连接 {0}"),
 (r"^Could not resolve host '(.+)'$", "无法解析主机「{0}」"),
]

# Tweak 侧 HUD（SpringBoard/Camera 进程）
EXACT.update({
 "TAP SCREEN NOW\nto record coordinates": "现在点击屏幕\n以录制坐标",
 "Recording tap in 1...": "1 秒后录制点击…",
 "Recording tap in 2...": "2 秒后录制点击…",
 "Recording tap in 3...": "3 秒后录制点击…",
 "last none": "无上次记录",
})
REGEX.insert(0, (r"^Recording tap in (\d+)\.\.\.$", "{0} 秒后录制点击…"))
REGEX.append((r"^last ([0-9.]+), ([0-9.]+)$", "上次 {0}, {1}"))
REGEX.append((r"^Tap Target \((\d+)\)$", "点击目标（{0}）"))
REGEX.append((r"^RemoteCompanion Tap Test\nhits (\d+)\n(.*)$", "RemoteCompanion 点击测试\n命中 {0}\n{1}"))

def esc(s):
    out = []
    for ch in s:
        o = ord(ch)
        if o < 128:
            out.append(ch.replace("\\", "\\\\").replace('"', '\\"'))
        else:
            # 拆代理对（ObjC \u 只支持 BMP）
            cp = o
            if cp > 0xFFFF:
                cp -= 0x10000
                hi = 0xD800 + (cp >> 10)
                lo = 0xDC00 + (cp & 0x3FF)
                out.append("\\u%04x\\u%04x" % (hi, lo))
            else:
                out.append("\\u%04x" % o)
    return "".join(out)

lines = []
lines.append("// RemoteCompanionCN - auto-generated by gen.py, do not edit by hand")
lines.append("#import <UIKit/UIKit.h>")
lines.append("")
lines.append("static NSDictionary *RCCNExact;")
lines.append("static NSArray *RCCNRegex;   // NSArray of (NSRegularExpression*, NSArray<NSString*>* templates)")
lines.append("")
lines.append("static NSString *RCCNTranslate(NSString *src) {")
lines.append("    if (!src || src.length == 0 || src.length > 400) return src;")
lines.append("    NSString *hit = RCCNExact[src];")
lines.append("    if (hit) return hit;")
lines.append("    for (NSArray *pair in RCCNRegex) {")
lines.append("        NSRegularExpression *re = pair[0];")
lines.append("        NSArray *templates = pair[1];")
lines.append("        NSTextCheckingResult *m = [re firstMatchInString:src options:0 range:NSMakeRange(0, src.length)];")
lines.append("        if (!m) continue;")
lines.append("        for (NSString *tpl in templates) {")
lines.append("            NSString *out = tpl;")
lines.append("            for (NSUInteger i = 0; i < m.numberOfRanges - 1 && i < 3; i++) {")
lines.append("                NSString *val = [src substringWithRange:[m rangeAtIndex:i + 1]];")
lines.append("                out = [out stringByReplacingOccurrencesOfString:[NSString stringWithFormat:@\"{%lu}\", (unsigned long)i] withString:val];")
lines.append("            }")
lines.append("            return out;")
lines.append("        }")
lines.append("    }")
lines.append("    return src;")
lines.append("}")
lines.append("")

# exact dict
lines.append("static void RCCNInit(void) {")
lines.append("    RCCNExact = [@{")
for k, v in EXACT.items():
    lines.append('        @"%s" : @"%s",' % (esc(k), esc(v)))
lines.append("    } copy];")
lines.append("    NSMutableArray *arr = [NSMutableArray array];")
for pat, tpl in REGEX:
    # template may contain multiple {0}
    parts = tpl.split("{0}")
    lines.append('    [arr addObject:@[ [[NSRegularExpression alloc] initWithPattern:@"%s" options:0 error:nil], @[@"%s"] ]];'
                 % (esc(pat), esc(tpl)))
lines.append("    RCCNRegex = arr copy;")
lines.append("}")
lines.append("")

# hooks
hooks = r"""
%hook UILabel
- (void)setText:(NSString *)text { %orig(RCCNTranslate(text)); }
%end

%hook UITextField
- (void)setPlaceholder:(NSString *)p { %orig(RCCNTranslate(p)); }
%end

%hook UIButton
- (void)setTitle:(NSString *)title forState:(UIControlState)state { %orig(RCCNTranslate(title), state); }
%end

%hook UIBarButtonItem
- (instancetype)initWithTitle:(NSString *)title style:(UIBarButtonItemStyle)style target:(id)target action:(SEL)action {
    return %orig(RCCNTranslate(title), style, target, action);
}
- (void)setTitle:(NSString *)title { %orig(RCCNTranslate(title)); }
%end

%hook UIAlertController
- (instancetype)initWithTitle:(NSString *)title message:(NSString *)message preferredStyle:(UIAlertControllerStyle)style {
    return %orig(RCCNTranslate(title), RCCNTranslate(message), style);
}
- (void)setTitle:(NSString *)title { %orig(RCCNTranslate(title)); }
- (void)setMessage:(NSString *)message { %orig(RCCNTranslate(message)); }
%end

%hook UIAlertAction
- (instancetype)initWithTitle:(NSString *)title style:(UIAlertActionStyle)style handler:(void (^)(UIAlertAction *))handler {
    return %orig(RCCNTranslate(title), style, handler);
}
- (void)setTitle:(NSString *)title { %orig(RCCNTranslate(title)); }
%end

%hook UITextField
- (void)setPlaceholder:(NSString *)placeholder {
    %orig(RCCNTranslate(placeholder));
}
%end

%hook UIBarButtonItem
- (instancetype)initWithTitle:(NSString *)title style:(UIBarButtonItemStyle)style target:(id)target action:(SEL)action {
    return %orig(RCCNTranslate(title), style, target, action);
}
- (void)setTitle:(NSString *)title { %orig(RCCNTranslate(title)); }
%end

%hook UIMenu
- (instancetype)initWithTitle:(NSString *)title image:(UIImage *)image identifier:(UIMenuIdentifier)identifier options:(UIMenuOptions)options children:(NSArray<UIMenuElement *> *)children {
    return %orig(RCCNTranslate(title), image, identifier, options, children);
}
%end

%hook UITableViewHeaderFooterView
- (void)setTextLabel:(UILabel *)label {
    UILabel *l = label;
    l.text = RCCNTranslate(l.text);
    %orig(l);
}
%end
"""

lines.append(hooks)
lines.append("")
lines.append("%ctor {")
lines.append("    RCCNInit();")
lines.append("}")
lines.append("")

open("RemoteCompanionCN.x", "w").write("\n".join(lines))
print("exact:", len(EXACT), "regex:", len(REGEX), "bytes:", len("\n".join(lines)))

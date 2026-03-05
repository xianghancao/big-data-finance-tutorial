import os

html_snippet_path = "_static/ai-assistant.html"
build_dir = "_build/html"

# 从系统的环境变量中获取真实 Token
# 如果你在本地测试没配置环境变量，它会暂时为空，避免报错
coze_token = os.environ.get("COZE_TOKEN", "未设置真实Token")

with open(html_snippet_path, "r", encoding="utf-8") as f:
    html_snippet = f.read()

# 在注入前，把占位符替换为真实的 Token
html_snippet = html_snippet.replace("__COZE_TOKEN_PLACEHOLDER__", coze_token)

for root, dirs, files in os.walk(build_dir):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # 注入到 </body> 之前
            if "</body>" in content and "7613756909895974946" not in content:
                content = content.replace("</body>", html_snippet + "\n</body>")
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                    
print("✅ AI 助手代码已成功注入，并已动态加载 Token！")
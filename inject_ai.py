# inject_ai.py
import os

html_snippet_path = "_static/ai-assistant.html" # 如果你把它放进了 _static 文件夹，这里就写 "_static/ai-assistant.html"
build_dir = "_build/html"

with open(html_snippet_path, "r", encoding="utf-8") as f:
    html_snippet = f.read()

for root, dirs, files in os.walk(build_dir):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # 安全地将代码注入到 </body> 标签之前
            if "</body>" in content and "id=\"ai-widget-container\"" not in content:
                content = content.replace("</body>", html_snippet + "\n</body>")
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                    
print("✅ AI 助手代码已成功注入到所有生成的网页中！")
# htmlTemplates.py

def base_template(title: str, content: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f9f9f9; }}
        .container {{ max-width: 800px; margin: auto; background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        {content}
    </div>
</body>
</html>
"""

def error_template(message: str) -> str:
    return base_template("Error", f"<p style='color:red;'>{message}</p>")

def success_template(message: str) -> str:
    return base_template("Success", f"<p style='color:green;'>{message}</p>")


css = """
<style>
    .container {
        max-width: 700px;
        margin: 30px auto;
        background: #fff;
        border-radius: 18px;
        box-shadow: 0 8px 32px rgba(60,60,60,0.12);
        padding: 32px 24px 24px 24px;
    }
    .chat-header {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 700;
        color: #0f5132;
        margin-bottom: 18px;
        letter-spacing: 1px;
    }
    .chat-message {
        display: flex;
        align-items: flex-start;
        margin-bottom: 18px;
        gap: 12px;
    }
    .chat-message.user {
        flex-direction: row-reverse;
        justify-content: flex-end;
    }
    .chat-message.bot {
        justify-content: flex-start;
    }
    .avatar {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        object-fit: cover;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border: 2px solid #d1e7dd;
    }
    .message-bubble {
        max-width: 75%;
        padding: 16px 22px;
        border-radius: 16px;
        font-size: 1.08rem;
        line-height: 1.6;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        margin-top: 2px;
        margin-bottom: 2px;
    }
    .chat-message.user .message-bubble {
        background: linear-gradient(90deg, #d1e7dd 80%, #b6dfc7 100%);
        color: #0f5132;
        border-bottom-right-radius: 4px;
    }
    .chat-message.bot .message-bubble {
        background: linear-gradient(90deg, #f1f0f0 80%, #e2e2e2 100%);
        color: #333;
        border-bottom-left-radius: 4px;
    }
    .chat-footer {
        text-align: center;
        color: #888;
        font-size: 0.95rem;
        margin-top: 24px;
    }
</style>
"""

bot_template = """
<div class="chat-message bot">
    <img src="https://cdn-icons-png.flaticon.com/512/4712/4712027.png" alt="Bot Avatar" class="avatar">
    <div class="message-bubble">{message}</div>
</div>
"""

user_template = """
<div class="chat-message user">
    <img src="https://cdn-icons-png.flaticon.com/512/9131/9131529.png" alt="User Avatar" class="avatar">
    <div class="message-bubble">{message}</div>
</div>
"""

error_template = """
<div class="chat-message bot">
    <img src="https://cdn-icons-png.flaticon.com/512/4712/4712027.png" alt="Bot Avatar" class="avatar">
    <div class="message-bubble" style="background: #ffe0e0; color: #b30000;">
        <strong>Error:</strong> {message}
    </div>
</div>
"""

success_template = """
<div class="chat-message bot">
    <img src="https://cdn-icons-png.flaticon.com/512/4712/4712027.png" alt="Bot Avatar" class="avatar">
    <div class="message-bubble" style="background: #e0ffe0; color: #0f5132;">
        <strong>Success:</strong> {message}
    </div>
</div>
"""

base_template = """
<div class="container">
    <div class="chat-header">📄 PDF QnA Bot</div>
    {content}
    <div class="chat-footer">Powered by Streamlit & LangChain</div>
</div>
"""

# Usage in Streamlit:
# st.write(css, unsafe_allow_html=True)
# st.write(base_template.format(content=bot_template.format(message="Ask me anything from your PDFs!")), unsafe_allow_html=True)


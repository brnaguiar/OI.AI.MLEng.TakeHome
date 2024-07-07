def get_root_html() -> str:
    return """
    <html>
        <head>
            <title>Marine Animal Predictor</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f2f9ff;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    color: #003366;
                }
                form {
                    display: inline-block;
                    background-color: #fff;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                input[type="text"], input[type="submit"] {
                    margin: 5px;
                    padding: 10px;
                    border-radius: 5px;
                }
                input[type="text"] {
                    border: 1px solid #003366;
                }
                input[type="submit"] {
                    background-color: #003366;
                    color: #fff;
                    border: none;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #00509e;
                }
            </style>
        </head>
        <body>
            <h1>Marine Animal Predictor</h1>
            <form action="/predict/" method="post">
                <input name="url" type="text" placeholder="Enter image URL">
                <input type="submit" value="Predict">
            </form>
        </body>
    </html>
    """


def get_prediction_html(prediction_class: str, url: str) -> str:
    return f"""
    <html>
        <head>
            <title>Prediction Result</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #e0f7fa;
                    text-align: center;
                    padding: 50px;
                }}
                h1 {{
                    color: #003366;
                }}
                .result {{
                    display: inline-block;
                    background-color: #fff;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }}
                img {{
                    max-width: 100%;
                    height: auto;
                    border: 1px solid #003366;
                    border-radius: 5px;
                }}
                .prediction {{
                    margin-top: 10px;
                    font-size: 1.2em;
                    color: #003366;
                }}
            </style>
        </head>
        <body>
            <h1>It's a {
                prediction_class+'!'
                if prediction_class != 'unknown class'
                else ':('
            }</h1>
            <div class="result">
                <img src="{url}" alt="Marine Animal Image">
            </div>
            <br>
            <a href="/">Go Back</a>
        </body>
    </html>
    <div class="prediction"></div>
    """

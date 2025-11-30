import streamlit as st
import pathlib

st.set_page_config(page_title="QRImage", layout="wide")

# Load files
html = pathlib.Path("index.html").read_text(encoding="utf-8")
css = pathlib.Path("index.css").read_text(encoding="utf-8")
js = pathlib.Path("index.js").read_text(encoding="utf-8")
qrcode_js = pathlib.Path("qrcode.js").read_text(encoding="utf-8")

# Force light theme
st.markdown("""
<style>
body, .stApp {
    background: white !important;
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# Correct execution order (IMPORTANT FIX) - REMOVE SCRIPT TAGS FROM index.html FIRST!
# NOTE: The html content you provided already includes the external links/tags inside the body, 
# so we will just embed the CSS and JS once, correctly.

# The index.html already has the structure, so let's use it as a base.
# 1. Remove the external links for CSS and JS files from index.html (you've already done this internally, but good to know)
# 2. Embed CSS in <head>
# 3. Embed qrcode.js and index.js just before </body>

# Clean up the original HTML to remove external file references (if they exist)
# NOTE: Based on the index.html you provided, you have:
# <link rel="stylesheet" href="index.css" />
# <script src="qrcode.js"></script>
# <script src="index.js"></script>
# These MUST be removed or ignored since you are embedding the code.

# To simplify, let's inject the necessary parts into the HTML structure you want:
html_content = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>QRImage</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
        <link rel="icon" href="./images/demo_squid.png" />
        <style>
        {css}
        </style>
    </head>
    <body>
        <div style="width: 50%; margin: 0 auto">
            <div class="center">
                <h1>QRImage</h1>
            </div>

            <div class="center">
                <h3>QRImage is a web app to generate QR codes with images.</h3>
            </div>

            <br />

            <label>Image File (optional):</label>
            <input type="file" id="imageLoader" name="imageLoader" />
            <p>
                Works better for square images (use an
                <a href="https://www.online-image-editor.com/">editor</a> as
                needed).
            </p>

            <div class="center">
                <canvas id="imageCanvas"></canvas>
            </div>

            <label>URL*:</label>
            <input class="w3-input" id="text" type="text" />

            <br />

            <div class="tooltip">
                Bit size:
                <span class="tooltiptext"
                    >Larger sizes hide more of the image, but are easier to
                    scan. I found that a size of 30 works well.</span
                >
                <span id="printSize"></span>
            </div>

            <br /><br />

            <div class="slidecontainer">
                <input
                    type="range"
                    min="10"
                    max="100"
                    value="30"
                    class="slider"
                    id="radiusSize"
                />
            </div>

            <br />

            <div class="tooltip">
                Error Correction:
                <span class="tooltiptext"
                    >Higher level of error correction makes bigger qr codes, but
                    also allows you to hide more of the QR code. The former is
                    more relevant to this app.</span
                >
                <span id="printCorrection"></span>
            </div>

            <br /><br />

            <div class="slidecontainer">
                <input
                    type="range"
                    min="1"
                    max="3"
                    value="3"
                    class="slider"
                    id="errorCorrection"
                />
            </div>

            <br />

            <div class="tooltip">
                Border Size:
                <span class="tooltiptext"
                    >Size of white border around QR code. Typically need some
                    border around the code, but depending on your use case you
                    can get rid of it.</span
                >
                <span id="printBorderSize"></span>
            </div>

            <br /><br />

            <div class="slidecontainer">
                <input
                    type="range"
                    min="0"
                    max="5"
                    value="0"
                    class="slider"
                    id="borderSize"
                />
            </div>

            <br />

            <input
                type="checkbox"
                id="whitebackground"
                name="whitebackground"
            />
            <label for="whitebackground">White background</label><br />

            <br />

            <div class="center">
                <button
                    class="w3-button w3-white w3-border w3-border-blue"
                    style="margin: 0 auto"
                    onclick="makeCode()"
                >
                    Generate QR code
                </button>
            </div>

            <br />

            <div class="center">
                <canvas id="myCanvas"></canvas>
            </div>

            <br />

            <div class="center">
                <button
                    class="w3-button w3-white w3-border w3-border-blue"
                    style="margin: 0 auto"
                    onclick="download()"
                >
                    Download PNG
                </button>
            </div>

            <div class="center">
                <p>
                    *Note that these QR codes may not work with every QR code
                    reader, so be sure to test them first. If you are having
                    trouble getting them to read, you may want to increase the
                    bit size.
                </p>
            </div>

            <br />
        </div>

        <a id="link"></a>
        <div id="qrcode" style="display: none"></div>
        
        <script>
        {qrcode_js}
        </script>
        <script>
        {js}
        </script>

    </body>
</html>
"""

st.components.v1.html(html_content, height=2500, scrolling=True)
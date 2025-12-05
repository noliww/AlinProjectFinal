import streamlit as st
from PIL import Image
import numpy as np
import cv2
import math

st.set_page_config(page_title="Geometric Transformations", layout="wide")

# -------------------------------------------------------------------
# PAGE TITLE
# -------------------------------------------------------------------
st.title("Geometric Transformations (Matrix-based)")

st.markdown("""
This page shows *geometric transformations* using *2D matrices*:

1. Translation  
2. Scaling  
3. Rotation  
4. Shearing  
5. Reflection  

### Affine Transformation Matrix (2×3)
""")

st.latex(r"""
M =
\begin{bmatrix}
a_{11} & a_{12} & t_x \\
a_{21} & a_{22} & t_y
\end{bmatrix}
""")

st.markdown("### Applied using:")

st.latex(r"""
\begin{bmatrix}
x' \\
y'
\end{bmatrix}
=
M
\cdot
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
""")

# -------------------------------------------------------------------
# UPLOAD IMAGE
# -------------------------------------------------------------------
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is None:
    st.warning("Please upload an image to begin.")
    st.stop()

# Load and show original image
image = Image.open(uploaded_file).convert("RGB")
img_array = np.array(image)
rows, cols = img_array.shape[:2]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Original Image")
    st.image(image, use_column_width=True)

# -------------------------------------------------------------------
# SIDEBAR CONTROLS
# -------------------------------------------------------------------
st.sidebar.header("Transformation Controls")

transform_type = st.sidebar.selectbox(
    "Choose a geometric transformation",
    ["Translation", "Scaling", "Rotation", "Shearing", "Reflection"]
)

M = None  # transformation matrix
transformed = img_array.copy()

# -------------------------------------------------------------------
# 1. TRANSLATION
# -------------------------------------------------------------------
if transform_type == "Translation":
    st.sidebar.markdown("### Translation parameters")
    tx = st.sidebar.slider("Translate X (pixels, right = +)", -cols, cols, 0, step=10)
    ty = st.sidebar.slider("Translate Y (pixels, down = +)", -rows, rows, 0, step=10)

    M = np.float32([[1, 0, tx],
                    [0, 1, ty]])

    transformed = cv2.warpAffine(img_array, M, (cols, rows))

# -------------------------------------------------------------------
# 2. SCALING
# -------------------------------------------------------------------
elif transform_type == "Scaling":
    st.sidebar.markdown("### Scaling parameters")
    sx = st.sidebar.slider("Scale X (horizontal)", 0.1, 3.0, 1.0, step=0.1)
    sy = st.sidebar.slider("Scale Y (vertical)", 0.1, 3.0, 1.0, step=0.1)

    M = np.float32([[sx, 0, 0],
                    [0, sy, 0]])

    new_cols = int(cols * sx)
    new_rows = int(rows * sy)
    transformed = cv2.warpAffine(img_array, M, (new_cols, new_rows))

# -------------------------------------------------------------------
# 3. ROTATION
# -------------------------------------------------------------------
elif transform_type == "Rotation":
    st.sidebar.markdown("### Rotation parameters")
    angle = st.sidebar.slider("Angle (degrees, positive = counter-clockwise)", -180, 180, 0, step=5)
    scale = st.sidebar.slider("Uniform scale", 0.1, 3.0, 1.0, step=0.1)

    center = (cols / 2, rows / 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)

    transformed = cv2.warpAffine(img_array, M, (cols, rows))

# -------------------------------------------------------------------
# 4. SHEARING
# -------------------------------------------------------------------
elif transform_type == "Shearing":
    st.sidebar.markdown("### Shearing parameters")
    shear_axis = st.sidebar.radio("Shear direction", ["X-axis", "Y-axis"])
    shear_factor = st.sidebar.slider("Shear factor", -1.0, 1.0, 0.0, step=0.1)

    if shear_axis == "X-axis":
        M = np.float32([[1, shear_factor, 0],
                        [0, 1, 0]])

        new_cols = int(cols + abs(shear_factor) * rows)
        transformed = cv2.warpAffine(img_array, M, (new_cols, rows))

    else:
        M = np.float32([[1, 0, 0],
                        [shear_factor, 1, 0]])

        new_rows = int(rows + abs(shear_factor) * cols)
        transformed = cv2.warpAffine(img_array, M, (cols, new_rows))

# -------------------------------------------------------------------
# 5. REFLECTION
# -------------------------------------------------------------------
elif transform_type == "Reflection":
    st.sidebar.markdown("### Reflection parameters")
    axis = st.sidebar.radio("Reflection axis", ["Vertical (left-right flip)", "Horizontal (up-down flip)"])

    if axis == "Vertical (left-right flip)":
        M = np.float32([[-1, 0, cols],
                        [0, 1, 0]])
        transformed = cv2.warpAffine(img_array, M, (cols, rows))

    else:
        M = np.float32([[1, 0, 0],
                        [0, -1, rows]])
        transformed = cv2.warpAffine(img_array, M, (cols, rows))

# -------------------------------------------------------------------
# SHOW TRANSFORMED IMAGE
# -------------------------------------------------------------------
with col2:
    st.subheader("Transformed Image")
    st.image(transformed, use_column_width=True)

# -------------------------------------------------------------------
# SHOW MATRIX
# -------------------------------------------------------------------
st.markdown("---")
st.subheader("Transformation Matrix (2×3)")

if M is not None:
    st.write("Matrix *M* used in the transformation:")
    st.write(M)
else:
    st.info("No transformation matrix to display yet.")

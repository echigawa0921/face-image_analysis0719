import streamlit as st
import io
import requests
from PIL import Image
from PIL import ImageDraw

st.title('顔画像解析アプリ')

subscription_key = '23e10c89452d4b5ca7cf7c1ce7f8b457'
assert subscription_key

face_api_url = 'https://20210718echigawa.cognitiveservices.azure.com/face/v1.0/detect'

uploaded_file = st.file_uploader("Choose on image...", type="jpg")

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    with io.BytesIO() as output:
        img.save(output , format="JPG")
        bainary_img = output.getvalue()
        
        headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': subscription_key}

        params = {
            'returnFaceId': 'true',
            'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
        }

        res = requests.post(face_api_url, params=params,headers=headers, data=bainary_img)

        results = res.json()
        for result in results:
            age = result['faceAttributes']['age']
            gender = result['faceAttributes']['gender']
            rect = result['faceRectangle']

            draw = ImageDraw.Draw(img)
            draw.rectangle([(rect['left'], rect['top']), (rect['left']+rect['width'],rect['top']+rect['height'])], fill=None, outline='green',width=5)
            text = age,gender
            print(text)

    st.image(img, caption='アップロード画像',use_column_width=True)
    st.title('詳細')
    st.write(f'年齢：{age}')
    st.write(f'性別：{gender}')

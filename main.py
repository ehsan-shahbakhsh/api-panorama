# import cv2
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
# from typing import List, Annotated
# import numpy as np
# import io

app = FastAPI()


@app.get('/')
def index():
    return {"success": True}


# @app.post('/panorama')
# async def panorama(files: List[UploadFile] = Annotated[bytes, File(...)]):
#     try:
#         images = [cv2.imdecode(np.fromstring(file.file.read(), np.uint8), flags=cv2.IMREAD_COLOR) for file in files]
#         for i in range(len(images)):
#             images[i] = cv2.resize(images[i], (0, 0), fx=0.4, fy=0.4)
#
#         stitchy = cv2.Stitcher.create()
#         (dummy, output) = stitchy.stitch(images)
#
#         if dummy == cv2.STITCHER_OK:
#             _, result = cv2.imencode('.png', img=output)
#
#             cv2.waitKey(0)
#
#             output_io = io.BytesIO(result)
#
#             return StreamingResponse(
#                 output_io,
#                 media_type='image/png',
#                 headers={"Content-Disposition": "attachment; filename=stitched_image.png"},
#             )
#         elif dummy == cv2.STITCHER_ERR_NEED_MORE_IMGS:
#             return JSONResponse(
#                 status_code=400,
#                 content={
#                     "success": False,
#                     "message": "برای تبدیل به عکس های بیشتری نیاز است"
#                 }
#             )
#         else:
#             return JSONResponse(
#                 status_code=400,
#                 content={
#                     "success": False,
#                     "message": "در تبدیل عکس مشکلی پیش آمده است"
#                 }
#             )
#     except:
#         return JSONResponse(
#             status_code=500,
#             content={
#                 "success": False,
#                 "message": "خطا در تبدیل عکس"
#             }
#         )

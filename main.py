# import cv2
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from typing import List, Annotated
# import numpy as np
# import io
# import imutils


app = FastAPI()


@app.get('/')
def index():
    return {'success': True}


# @app.post('/panorama')
# async def panorama(files: List[UploadFile] = Annotated[bytes, File(...)]):
#     try:
#         print('hi2')
#         images = [cv2.imdecode(np.fromstring(file.file.read(), np.uint8), flags=cv2.IMREAD_COLOR) for file in files]
#         for i in range(len(images)):
#             images[i] = cv2.resize(images[i], (0, 0), fx=0.4, fy=0.4)

#         stitchy = cv2.Stitcher.create()
#         (dummy, stitched) = stitchy.stitch(images)
#         print('hi')

#         if dummy == cv2.STITCHER_OK:
#             stitched = cv2.copyMakeBorder(stitched, 10, 10, 10, 10, cv2.BORDER_CONSTANT, (0, 0, 0))

#             gray = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
#             thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

#             cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#             cnts = imutils.grab_contours(cnts)
#             c = max(cnts, key=cv2.contourArea)
#             # allocate memory for the mask which will contain the
#             # rectangular bounding box of the stitched image region
#             mask = np.zeros(thresh.shape, dtype="uint8")
#             (x, y, w, h) = cv2.boundingRect(c)
#             cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

#             minRect = mask.copy()
#             sub = mask.copy()
#             # keep looping until there are no non-zero pixels left in the
#             # subtracted image
#             while cv2.countNonZero(sub) > 0:
#                 # erode the minimum rectangular mask and then subtract
#                 # the thresholded image from the minimum rectangular mask
#                 # so we can count if there are any non-zero pixels left
#                 minRect = cv2.erode(minRect, None)
#                 sub = cv2.subtract(minRect, thresh)


#             cnts = cv2.findContours(minRect.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#             cnts = imutils.grab_contours(cnts)
#             c = max(cnts, key=cv2.contourArea)
#             (x, y, w, h) = cv2.boundingRect(c)
#             # use the bounding box coordinates to extract the our final
#             # stitched image
#             stitched = stitched[y:y + h, x:x + w]

#             _, result = cv2.imencode('.png', img=stitched)

#             cv2.waitKey(0)

#             output_io = io.BytesIO(result)

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
#                     "error": "need_more_images",
#                     "message": "برای تبدیل به عکس های بیشتری نیاز است"
#                 }
#             )
#         else:
#             return JSONResponse(
#                 status_code=400,
#                 content={
#                     "success": False,
#                     "error": "something_went_wrong",
#                     "message": "در تبدیل عکس مشکلی پیش آمده است"
#                 }
#             )
#     except:
#         return JSONResponse(
#             status_code=500,
#             content={
#                 "success": False,
#                 "error": "something_went_wrong",
#                 "message": "خطا در تبدیل عکس"
#             }
#         )

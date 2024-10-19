from pymongo import MongoClient
from datetime import datetime

#Buoc 1: kết nối đến MôngDB
client = MongoClient('localhost', 27017)
db = client['tiktok1'] # chọn csdl tiktok

#Bước 2: Tạo các collections
users_collection = db['users']
videos_collection = db['videos']

#Bước 3: thêm DL người dùng
users_data = [
    {'user_id': 1, 'username': 'user1', 'full_name': 'Nguyen Van A', 'followers': 1500, 'following': 200},
    {'user_id': 2, 'username': 'user2', 'full_name': 'Tran Thi B', 'followers': 2000, 'following': 300},
    {'user_id': 3, 'username': 'user3', 'full_name': 'Le Van C', 'followers': 500, 'following': 100}
]
users_collection.insert_many(users_data)

#Bước 4: thêm DL về video
videos_data = [
    {'video_id': 1, 'user_id': 1, 'title': 'Video 1', 'views': 10000, 'likes': 500, 'created_at': datetime(2024, 1, 1)},
    {'video_id': 2, 'user_id': 2, 'title': 'Video 2', 'views': 20000, 'likes': 1500,
     'created_at': datetime(2024, 1, 5)},
    {'video_id': 3, 'user_id': 3, 'title': 'Video 3', 'views': 5000, 'likes': 200, 'created_at': datetime(2024, 1, 10)}
]
videos_collection.insert_many(videos_data) # thêm DL video
# Bước 5: Truy vấn DL
#5.1: xem tất cả người dùng
print("Tất cả người dùng: ")
for user in users_collection.find():
    print(user)
# 5.2: tìm video có nhiều người xem nhất
mosted_viewed_video = videos_collection.find().sort('view', -1).limit(1)
for user in mosted_viewed_video:
    print(user)

#tìm tất cả video của người dùng có username là "user1"
print("/n Tất cả video của người dùng'user1': ")
user_videos = videos_collection.find({'user_id': 1})
for video in user_videos:
    print(video)

# bước 6: cập nhật DL
# cập nhật số người theo dõi của người dùng với 'user_id' là lên 2000
users_collection.update_one({'user_id': 1}, {'$set': {'followers': 2000}})

# Bước 7: Xóa video có `video_id` là 3
videos_collection.delete_one({'video_id': 3})

# Bước 8: Xem lại dữ liệu sau khi cập nhật và xóa
print("\nDữ liệu người dùng sau khi cập nhật:")
for user in users_collection.find():
    print(user)

print("\nDữ liệu video sau khi xóa:")
for video in videos_collection.find():
    print(video)

# Đóng kết nối
client.close()
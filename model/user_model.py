import mysql.connector
import json
from pytube import YouTube
class user_model():
    def __init__(self):
        #connection establishment
        try:
            self.con = mysql.connector.connect(host="localhost",username="root" , password="" , db="blogs")
            
            self.con.autocommit = True
            self.cur=self.con.cursor(dictionary=True)
        except:
            print("something went wrong with connection...")    
    def user_signup_model(self):
        return "this is signup function from model"
    def user_fetch_model(self):
        try:
            self.cur.execute("SELECT * FROM articles")
            result = self.cur.fetchall()
            if len(result) > 0:
                print(result)
                return json.dumps(result)
                # return "hello"
            else:
                return "No Data Found"
        except NameError:
            print(NameError)
    def user_add_model(self , data):
        try:
            sql = (f"INSERT INTO articles (title, subtitle, Description, Article_Author, published_date) "
               f"VALUES ('{data['title']}', '{data['subtitle']}', '{data['description']}', '{data['Article_Author']}', '{data['published_date']}')")
            result = self.cur.execute(sql)
            if(result):
                print("yes")
            else:
                print("no")
            return sql
        except NameError:
            return "something is not right"
     
    def download_youtube_video_model(self, url):
        try:
            video_url = url
            print('URL:', video_url)
            
            # Initialize a YouTube object with the video URL
            yt = YouTube(video_url)
            
            # Get the highest resolution stream available
            stream = yt.streams.get_highest_resolution()
            
            # Download the stream
            stream.download()
            
            # Optional: Return True or any success indication if needed
            return True
        except Exception as e:
            # Handle exceptions such as invalid URLs, network errors, etc.
            print(f"Error downloading video: {e}")
            return False

import http.server
import socketserver
import time
import os
# from config.py import PORT # type: ignore
PORT = 12345

PUBLIC_DIR = "D:\\p\\WEBSITE" 



class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        
        current_time = time.time() - start_time  
        elapsed_time = time.strftime("%H:%M:%S", time.gmtime(current_time))

        
        print(f'Requisição para: {self.path} | Execution Time: {elapsed_time}')

        
        if self.path == '/':
            self.path = '/index.html' 

        
        return super().do_GET()

    def get_content_type(self, path):
        
        if path.endswith('.html'):
            return 'text/html; charset=utf-8'
        elif path.endswith('.txt'):
            return 'text/plain; charset=utf-8'
        elif path.endswith('.json'):
            return 'application/json; charset=utf-8'
        elif path.endswith('.png'):
            return 'image/png'
        elif path.endswith('.jpg') or path.endswith('.jpeg'):
            return 'image/jpeg'
        elif path.endswith('.css'):
            return 'text/css; charset=utf-8'
        else:
            return 'application/octet-stream' 

    def log_message(self, format, *args):
        
        pass  



if __name__ == "__main__":
    start_time = time.time() 
    os.chdir(PUBLIC_DIR)

    


    print(f'Servidor iniciado em: http://127.0.0.1:{PORT}')
    print(f'Diretório público definido: {PUBLIC_DIR}')

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        httpd.serve_forever()


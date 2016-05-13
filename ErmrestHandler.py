__author__ = 'anurag'
import requests
import json


class ErmrestHandler(object):
    def __init__(self, host, username, password):
        self.host = host
        self._cookie = {"ermrest": self.get_cookie(username, password)}

    def get_cookie(self, username, password):
        r = requests.post('http://'+self.host+'/ermrest/authn/session',
                          data={'username': username,
                                'password': password})
        r.raise_for_status()
        return r.text[:-1]

    def create_catalog(self):
        pass

    def create_schema(self, name):
        pass

    def create_table(self, name):
        pass

    def get_data(self, catalog_id, table_name, user_name):
        r = requests.get("http://"+self.host+"/ermrest/catalog/"+str(catalog_id)+"/entity/"+
                         table_name+"/user="+user_name, cookies=self._cookie)
        return json.loads(r.text)

    def delete_data(self, catalog_id, table_name, user_name):
        r = requests.delete("http://"+self.host+"/ermrest/catalog/"+str(catalog_id)+"/entity/"+
                         table_name+"/user="+user_name, cookies=self._cookie)
        return json.loads(r.text)

    def put_data(self, catalog_id, table_name, data):
        data = [data]
        r = requests.put("http://"+self.host+"/ermrest/catalog/"+str(catalog_id)+"/entity/"+table_name,
                         json=data, cookies=self._cookie)

        r.raise_for_status()


if __name__ == '__main__':
    conn = ErmrestHandler('ec2-54-172-182-170.compute-1.amazonaws.com', 'root', 'root')
    conn.delete_data(1, 'sample7', 'Anoop')

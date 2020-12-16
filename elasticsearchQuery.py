#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def ES_veri(index,source=0):
    es = Elasticsearch(hosts=["http://elastic:*****@192.168.*:9200/",
                              "http://elastic:***@192.168.*:9200/",
                              "http://elastic:**@192.168.*:9200/"],timeout=50)
    
    some_query={
        'query':{
            "bool": {
            "must": [ ],
      "filter": [
        {
          "match_all": {
              
          }
        },
           {
          "range": {
               "timestamp": {
                  "gte": "now-2m",
                  "lte": "now",
                  "format": "yyyy-MM-dd HH:mm"
                
             }
          }
        }
      ],
      "should": [],
      "must_not": []
    }}}
    
    if source==0:
        res=es.search(index=index,body=some_query,scroll="5m",size=500000) #size=row sayısı
    elif source!=0:
        res=es.search(index=index,_source=source, body=some_query,scroll="5m",size=500000) #size=row sayısı
        
    #source=which paramater to get
    #The scroll parameter tells Elasticsearch to keep the search context open for another 1m.
    
    results=[]
    for hit in res['hits']['hits']:
        result=hit['_source']
        results.append(result)
        
    df=pd.DataFrame(results)
    
    df['date']=df.apply(lambda row: datetime.fromtimestamp((row.timestamp)/1000),axis=1)
    df['ID'] = df.apply(lambda row: row.timestamp/10000, axis = 1)
    
    
    return df


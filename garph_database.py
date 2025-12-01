from neo4j import GraphDatabase

# Ganti 'neo4j' (kecil semua) sebagai username
# Password tetap yang kamu punya
uri = "neo4j://127.0.0.1:7687" 
auth = ("neo4j", "badsfarmil232615") 

try:
    driver = GraphDatabase.driver(uri, auth=auth)
    driver.verify_connectivity()
    print("✅ SUKSES! ALHAMDULILLAH!")
except Exception as e:
    print(f"❌ Masih gagal: {e}")
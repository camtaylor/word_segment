from wordsegment import segment

if __name__ == "__main__":
  
  domains = []
  with open('temp', 'rb') as f:
    domains = f.readlines()
  
  for domain in domains:
    print " ".join(segment(domain))

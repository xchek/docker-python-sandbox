#!/usr/bin/env python3
import requests
import json


def main():
  r = requests.get(
    "https://www.boredapi.com/api/activity",
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
  )
  print(json.dumps(r.json(), indent=2))
  return


if __name__ == "__main__":
  main()

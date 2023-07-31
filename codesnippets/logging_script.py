while True:
  humidity,temperature = Rockfruit_DHT.read_retry(sensor,pin,retries=15)
  timestamp = datetime.datetime.now()
  if humidity is not None and temperature is not None:
    c.execute(
      "INSERT INTO readings VALUES (?, ?, ?, ?)",
      (
        timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        int(timestamp.timestamp()),
        temperature,
        humidity,
      ),
    )
    conn.commit()
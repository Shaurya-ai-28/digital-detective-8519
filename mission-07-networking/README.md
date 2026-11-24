# Mission 7 — How Computers Communicate

## 1. Task / objective
Learn basic computer networking concepts, run connectivity and DNS lookup tests, and describe what happens when opening a website.

## 2. Work completed
- Completed the network concepts table with plain explanations and examples.
- Documented `ping` and `nslookup` outputs.
- Wrote down the 7 steps of opening a website using **client**, **server**, **DNS**, and **protocol**.

---

### Task 7.1 — Explain Network Concepts

| Concept | Explanation | Example |
| :--- | :--- | :--- |
| **LAN** | Network covering a small local area. | Home Wi-Fi connecting laptop and phone. |
| **MAN** | Network covering a campus or city. | Campus network across college buildings. |
| **WAN** | Large network covering countries or the globe. | The global Internet. |
| **DNS** | Translates domain names into IP addresses. | Translating `google.com` to `142.250.190.46`. |
| **Router** | Forwards data packets between networks. | Home Wi-Fi router (`192.168.1.1`). |
| **Protocol** | Standard rules for communication. | HTTPS protocol for secure web traffic. |
| **Packet switching** | Splitting data into packets sent over networks. | Streaming video sent as small TCP/IP packets. |
| **Client-server** | Client requests service, server provides it. | Browser (client) requesting page from web server. |

---

### Task 7.2 — Observe Network Information

**1. Connectivity (`ping`):**
```bash
$ ping -c 3 google.com
3 packets transmitted, 3 received, 0.0% packet loss, ~18 ms latency
```
Checks if remote server is reachable, measures packet loss, and tests response time (latency).

**2. DNS Lookup (`nslookup`):**
```bash
$ nslookup google.com
Server: 8.8.8.8
Address: 142.250.190.46
```
Shows the DNS server consulted and the IP address mapped to the domain.

**Role of DNS:** Humans remember names like `google.com`, but routers need IP addresses. DNS translates names into numbers so browsers can connect.

---

### Task 7.3 — What Happens When You Open a Website?
1. **User types URL:** User enters `https://google.com` in the browser (**client**).
2. **DNS lookup:** The client queries a **DNS** server using the DNS **protocol** to get the IP address (`142.250.190.46`).
3. **TCP connection:** Client connects to the **server** via the local router using the TCP **protocol**.
4. **Security handshake:** Client and server negotiate encryption using the TLS **protocol**.
5. **HTTP request:** Client sends an HTTP GET request (HTTPS **protocol**) for the web page.
6. **Server response:** Web **server** returns the HTML, CSS, and assets in data packets (HTTP 200 OK).
7. **Rendering:** Client browser reassembles packets and displays the page.

---

## 3. Commands / tools used
- `ping -c 3 google.com`, `nslookup google.com`

## 4. My understanding
Networks use layered protocols so devices can communicate reliably across the world in milliseconds.

## 5. Difficulties faced
Distinguishing domain names from IP addresses.

## 6. How I resolved them
Domain names are human names; IP addresses are network phone numbers.

## 7. Evidence / files
- Diagnostic logs and 7-step website trace recorded above.

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Branch:** `main`

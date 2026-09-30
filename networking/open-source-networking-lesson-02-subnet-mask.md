---
title: "Open-Source Networking Lesson #2: What Is a Subnet Mask?"
status: published
wordpress_post_id: 19595
published: "2026-09-30T14:33:13"
live_url: "https://bitcoinversus.tech/2026/09/30/open-source-networking-lesson-2-subnet-mask/"
series: "Open-Source Networking"
lesson_number: 2
featured_media_id: 19597
featured_image_dimensions: "1200x630"
youtube: "https://www.youtube.com/watch?v=s_Ntt6eTn94&t=71s"
---

# Open-Source Networking Lesson #2: What Is a Subnet Mask?

A **subnet mask** works with an IP address to help identify the network portion and the host portion.

This lesson follows Open-Source Networking Lesson #1: What Is an IP Address?

## A Simple Example

```text
IP address:  192.168.1.25
Subnet mask: 255.255.255.0
```

For this beginner example, `192.168.1` identifies the local network and `25` identifies this host.

## Why the Mask Matters

A computer needs to decide whether another IP address is on the same local network or whether traffic needs to go toward a router. The subnet mask helps make that distinction.

## Video: Subnet Masks Explained Visually

PowerCert Animated Videos — Subnet Mask Explained, starting near its subnet-mask section:

https://www.youtube.com/watch?v=s_Ntt6eTn94&t=71s

## Same Network Example

```text
Computer: 192.168.1.25
Printer:  192.168.1.50
Mask:     255.255.255.0
```

Both devices share the `192.168.1` network portion in this example.

## Different Network Example

```text
Computer: 192.168.1.25
Server:   192.168.2.20
Mask:     255.255.255.0
```

The network portions differ, so communication between them normally goes through a router.

## Data Center Example

A technician may see a miner, server, switch-management interface, or laptop configured with an IP address and subnet mask. Checking both values helps confirm whether devices are intended to be on the same local network.

## Practice

1. Write down `192.168.10.15` with mask `255.255.255.0`.
2. Write down `192.168.10.40` with the same mask.
3. Identify the matching network portion.
4. Change the second address to `192.168.11.40`.
5. Identify what changed.

## Key Takeaway

A subnet mask works with an IP address to identify the network and host portions. With the common beginner example `255.255.255.0`, addresses sharing the first three octets are in the same local subnet.

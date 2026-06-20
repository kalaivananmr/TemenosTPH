# Introduction to Request to Pay (RtP)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/RF/Request_to_Pay/MISC/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Request to Pay > Introduction

- Request to Pay;)
  - [Introduction](../../Request_to_Pay/MISC/Introduction.htm)
  - Request Initiation;)
  - Request Approval;)
  - Bulk Upload;)
  - Recall;)
  - Investigation;)
  - Information Request;)
  - Reports;)
  - Interfaces and Message Standards;)
  - Charges;)
  - Scheme Manager;)
  - Notification;)
  - Reachability Check;)
  - Proxy Identifier;)
  - Pre Authorisation;)

Payments

# Introduction to Request to Pay (RtP)

Updated On 22 March 2025 |
 4 Min(s) read

Feedback
Summarize

Temenos Request to Pay solution is an integral part of the Temenos Payment. Temenos RtP assists the user in payment request initiation and approvals. Temenos RtP solution enables the user to view and manage their RtP request on behalf of the payee and the payer. It also provide APIs for integration with the bank’s front end channel. The module is available as a part of Temenos Transact with license code ‘RF’.



- Customer Facing Systems support the customer facing channels through
  - Initiating and responding to RtP request from online Channel (through API)
  - Receiving bulk RtP requests (manual upload or from queue)
  - Enquiring about the RtP request from online channel (through API)

- The RtP system has the following functionality
  - Receives a request for payment from the payee using standard Temenos Transact interface, validates, enriches, and routes them to appropriate payer RtP system through clearings or direct post to payer RtP provider.
  - For a payer, the RtP application receives a request from the payee through the clearing or direct post to payer RtP provider and awaits for payer action.
  - If the payer approves the request, then the RtP system captures the payment request in the PAYMENT.ORDER application and routes the payment to the appropriate payment system.
  - Generates request to pay status and updates as customer notification for payee or payer.

- The PO application has the following functionality

  Once the payer accepts the request, the PO application captures the payment request in the PO application and routes to the payment system. When the payment is completed, the payment status is communicated with the RtP application.

- Payment System has the following functionality.

  The payment system (such as Temenos Payments Hub or bank’s non-Temenos Payment system) validates, books, and routes the payment to an appropriate clearing system.

- Core Banking

  Bank’s core banking that supports account related validation of the RtP request.

- RtP Clearings

  The RtP application is capable of interacting with payee or payer RtP system either through a centralised system or directly through APIs in an open banking system.

## RtP Participants

The following table shows the participants involved in the lifecycle of RtP.

| Participant | Description |
| --- | --- |
| Payee | Entity that creates an RtP adhering to a scheme |
| Payer | Entity that consumes the RtP and required to make the payment |
| Payee Bank | Payee financial institution that receives, stores, and forwards the RtP messages. Also, provides the front-end GUI for the payee |
| Payer Bank | Payer’s financial institution that provides flexibility to respond to RtP messages. Acts as front-end channel for payer to send and receive the RtP messages and make payments |
| Central Infrastructure (CI) | Entity that plays a role in storing and forwarding RtP messages of a payee |

## Supported Clearings

RtP framework supports the following Clearings:

- [Europe (EBA R2P)](../../../../Request_to_Pay/EBA_R2P/RTP_Clearing/EBA_Request_to_Pay/Introduction.htm)
- [United Kingdom (Pay UK)](../../../../Request_to_Pay/RTP_UK/RTP_Clearing/United_Kingdom_EAP_RFPYUK/Introduction.htm)
- [Saudi Arabia (Saudi RTP)](../../../../Request_to_Pay/SAIPS/RTP_Clearing/Saudi_Arabia_RFPYSA/Introduction.htm)

In this topic

- [Introduction to Request to Pay (RtP)](#IntroductiontoRequesttoPayRtP)

- [RtP Participants](#RtPParticipants)
- [Supported Clearings](#SupportedClearings)




Copyright © 2020-2026 Temenos Headquarters SA

Cookie Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:17:14 PM IST
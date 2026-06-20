# Introduction to Pay UK Request to Pay (EAP)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Request_to_Pay/RTP_UK/RTP_Clearing/United_Kingdom_EAP_RFPYUK/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   United Kingdom > Pay UK - Request to Pay (EAP) > Introduction

- United Kingdom;)
  - Pay UK - Request to Pay (EAP);)
    - [Introduction](../../RTP_Clearing/United_Kingdom_EAP_RFPYUK/Introduction.htm)
    - [Configuration](../../RTP_Clearing/United_Kingdom_EAP_RFPYUK/Configuration.htm)
    - [Working with](../../RTP_Clearing/United_Kingdom_EAP_RFPYUK/Working_with.htm)
    - [Tasks](../../RTP_Clearing/United_Kingdom_EAP_RFPYUK/Tasks.htm)
    - [Outputs](../../RTP_Clearing/United_Kingdom_EAP_RFPYUK/Outputs.htm)

Payments

# Introduction to Pay UK Request to Pay (EAP)

Updated On 08 August 2022 |
 6 Min(s) read

Feedback
Summarize

In the Pay UK scheme, End User Applications (EAP) provides a front-end (channel solution) to customers to perform various actions that results in message exchange between the requestor or payee and payer through their respective RSPs.

Temenos RtP acts as a server-side supplementing solution for the bank’s EAP (payer side) allowing it to connect to an established Pay UK repository (RSP) to which the payer is registered and exchange UK RtP messages such as RtP requests, payer’s approval messages, due date extension requests and notes. Similarly, any response received from the requestor or payee is fetched from the repositories.

Temenos RtP solution provides back-end processing for EAP solutions that act as front-end for customers. It does not provide front-end interfaces.

## Roles and Participants

Pay UK RtP Repository Service Provider (RSP) supports pre-defined roles and participants to operate the messaging service. The following table explains the roles and their responsibilities.

| Role | Definition |
| --- | --- |
| Request to pay end user | Entity involved in initiating or receiving RtP messages |
| Repository operator | Organisation enabling storage and exchange of RtP messages (RSP) |
| Application provider | Organisation providing front-end application to send and retrieve messages. Organisation providing EAP |
| Payments Service Provider (PSP) | Organisation established primarily to provide payments services |

Temenos RtP solution is used by banks that provide an EAP solution for their customers, by enabling RtP message exchanges with the RSP.

The following table explains the participants and their responsibilities.

| Participant | Definition |
| --- | --- |
| Payee or biller | The person who initiates the RtP message and to whom the money is to be paid |
| Payer | The person who pays the bill. A payer responds to the RtP message |
| Payee or biller’s application provider | Entity that offers a front-end channel for the biller to send and receive RtP messages |
| Payer’s application provider | Entity that offers a front-end channel for the payer to send and receive RtP messages |
| Payee or biller’s repository operator | Entity that stores and forwards the RtP messages of a payee or biller |
| Payer’s repository operator | Entity that stores and forwards the RtP messages of a payer |
| Payee or biller’s PSP | Payee's or biller’s financial institution |
| Payer’s PSP | Payer’s financial institution |

[Channel Integration](#)

Temenos RtP solution for bank’s EAP (payer side) receives the following requests from the payer’s front-end channel through API.

- Refresh requests for retrieving RtP data from RSP
- Payer’s response for RtP
- Extension requests for due date
- Send notes to payee or biller

Refer [API Catalog](https://apidocs.temenos.com/) for more details on available APIs.

[Refresh Request](#)

Payer can request to refresh the available RtP information in Temenos RtP solution since their last login in the front-end application. Upon receiving a refresh request, Temenos RtP solutions connect with the payer’s repository operator to:

- Retrieve new RtPs available on the repository.
- Update existing RtPs available in Temenos RtP solution, with any new messages from the repository.

## RtP Processing Workflows

The following diagrams explain the RtP refresh and request workflow.

[Inward Processing – RtP Refresh](#)

The inward processing (initiation) of RtP Refresh is described in the below flowchart.



| Activity | Description |
| --- | --- |
| Receive proxy ID and access token from channel for payer | Receive payer’s PID and access token to connect with payer’s repository operator.  Channel should authenticate the payer with RSP and obtain an access token and pass it to Temenos RtP. |
| Connect to payer’s RSP | Once the RtP refresh request is received from the payer’s channel, the system connects to the payer’s RSP using payer’s PID and access token. |
| Retrieve RTPs from payer’s RSP | RtP requests received for the payer are fetched from the payer’s RSP. |
| Validate | The system performs the following validations:   - Account Validation – Validates the validity and restrictions of the payer account. - Date   Validation – Validates the requested execution date against the expiry date. |
| Store RTP requests | New RtP requests received for the payer are stored in Temenos local data store. |
| Update RTP requests | Update existing RtPs in Temenos local data store with new messages from payer’s repository. |

[Outward Processing – RtP Response](#)

The outward processing (reception) of the RtP is described in the below flowchart.



| Activity | Description |
| --- | --- |
| RTPs awaiting user response | On receiving an RtP fetch request from the payer’s channel, Temenos RtP solution fetches new RtP requests and updates the existing RtPs with new messages from Temenos RtP data store. |
| Payer approval or decline | Payer can respond to the RtP request to either approve (pay all or pay partial) or decline. |
| Update status to approved or declined | Based on the payer’s response, RtP status is updated. |
| Generate payment | When the payer approves a RtP request (pay all or pay partial), a payment request is generated and sent to the payment system (TPH or any other payment system) to process the payment. |
| Update payer RSP about approval | On successful payment, the payer’s RSP is updated with payer’s approval. |
| Update status as payment failed | If the generated payment fails, the RtP status is updated as Unpaid, for the payer to retry the payment. |
| Update payer RSP about decline | When the payer declines a RtP request, it is updated to the payer’s RSP. |

In this topic

- [Introduction to Pay UK Request to Pay (EAP)](#IntroductiontoPayUKRequesttoPayEAP)

- [Roles and Participants](#RolesandParticipants)
- [RtP Processing Workflows](#RtPProcessingWorkflows)




Copyright © 2020-2026 Temenos Headquarters SA

Cookie Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:30:54 PM IST
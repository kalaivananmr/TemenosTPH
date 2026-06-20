# Introduction to EBA Request to Pay (R2P)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Request_to_Pay/EBA_R2P/RTP_Clearing/EBA_Request_to_Pay/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > EBA Request to Pay (R2P) > Introduction

- Europe;)
  - EBA Request to Pay (R2P);)
    - [Introduction](../../RTP_Clearing/EBA_Request_to_Pay/Introduction.htm)
    - [Configuration](../../RTP_Clearing/EBA_Request_to_Pay/Configuring.htm)
    - [Working with](../../RTP_Clearing/EBA_Request_to_Pay/Workingwith.htm)
    - [Tasks](../../RTP_Clearing/EBA_Request_to_Pay/Tasks.htm)
    - [Outputs](../../RTP_Clearing/EBA_Request_to_Pay/Outputs.htm)

Payments

# Introduction to EBA Request to Pay (R2P)

Updated On 10 July 2024 |
 10 Min(s) read

Feedback
Summarize

Request to Pay (R2P) by Euro Banking Association (EBA) Clearing is a Pan-European real time messaging service for exchanging Request to Pay messages. The EBA Request to Pay is a feature-loaded service that benefits both Payee and Payer. The Payee, Biller or Requestor can use the R2P service to request payment for goods or services availed by the Payer. This user guide provides an overview of the Temenos RtP solution for EBA R2P.

The below table represents the participants of EBA request to pay.

| Participants | Description |
| --- | --- |
| Payee, Biller or Requestor | The customer who initiates the payment request to a Payer |
| Payer | The customer who receives the payment request from Payee for approval |
| Payee Service Provider | The service provider that processes the payment request messages for the Payee |
| Payer Service Provider | The service provider that processes the payment request messages for the Payer |
| EBA R2P | The central system through which R2P messages are exchanged and processed between the payee and payer service provider |

Temenos RtP solution can act as a service provider for both payee and payer.

[Message Types](#)

The below table represents the message types for EBA R2P supported by Temenos RtP solution .

| Message Type | Version | Description |
| --- | --- | --- |
| Request | pain.013.001.07 | The message format for initiating payment requests by Payee Service Provider |
| Confirmation Response | pain.014.001.07 | The message format to confirm payment request by Payer Service Provider |
| Approval Response | pain.014.001.07 | The message format to convey the payer’s acceptance of payment request by the Payer Service Provider |
| Rejection Response | pain.014.001.07 | The message format to convey the payer’s rejection of payment request by the Payer Service Provider |
| Cancellation | camt.055.001.08 | The message format for initiating cancellation of payment request by Payee Service Provider |
| Cancellation response | camt.029.001.09 | The message format for conveying a response to the cancellation request by Payer Service Provider |
| Investigation on a Request | pacs.028.001.03 | The message format to enquire on the status of payment request by the Payee Service Provider |
| Response to an Investigation on a Request | pain.014.001.07 | The message format for responding with the status of payment request by the Payer Service Provider |
| Investigation on a cancellation | camt.055.001.08 | The message format to enquire on the status of the cancellation request sent by the Payee Service Provider |
| Response to an Investigation on a cancellation | camt.029.001.09 | The message format for responding with the cancellation status sent by Payer Service Provider |

[EBA R2P Message Flow](#)

The below diagram shows the flow of the EBA R2P message between the Payee Bank and Payer Bank.



[Use Cases](#)

Temenos RtP solution supports the below use cases of EBA R2P.

| Use cases | Description |
| --- | --- |
| Approve Now | The payee can initiate a request which requires approval from the payer within short timelines. This use case may ideally support business scenarios in real-time situations (for example, a payment request at a convenience store for checkout). |
| Approve Later / Request to Pay Plus | The payee can initiate a request for which the payer has a longer time frame to respond. This use case may ideally support business scenarios that do not require immediate approval from the payer (for example, utility bill payments). |

[Additional Optional Services](#)

Temenos RtP solution supports ALIAS Additional Optional Service (AOS) offered by EBA R2P.

The payee can utilize the ALIAS service if the payee and payer banks have subscribed to the respective additional service of the EBA R2P.

Subscription to ALIAS AOS permits the payee to provide a proxy instead of the Payer’s IBAN (International Banking Account number) in the request. The payer bank should resolve the proxy of the Payer and the approval response sent by the payer bank should contain the IBAN of the Payer.

[Key Characteristics Supported for RtP Processing](#)

The key characteristics supported for RtP processing are given below.

| Key Characteristics | Description |
| --- | --- |
| Amount Modification | The payee can specify whether the payer can modify the payable amount for the payment request |
| Early Payment | The payee can specify whether the payer can make an early payment.  If permitted by the payee, the payer can make payment before the specified requested execution date or time by the payee.  If not permitted by the payee, the payer can make the payment after the requested execution date or time. |
| Payment Instrument | The payee can specify the accepted payment instrument and whether the payer is allowed to change the payment instrument.  Temenos RtP solution supports SCT (SEPA (Single Euro Payments Area) Credit Transfer) and SCT Inst (SEPA Instant Credit Transfer) payment instruments. |

[Reachability](#)

Before initiating an EBA, the Payee bank performs a reachability check of the payer bank based on the Business Identifier Code (BIC). The reachability is determined based on the routing file provided by the EBA R2P clearing, which the user should upload to the clearing directory. Temenos RtP solution for EBA R2P supports only the direct participants of the EBA R2P service.

The user should specify the EB.FILE.UPLOAD.TYPE as EBARTPDIR. Read [Clearing Directory](https://docs.temenos.com/docs/Solutions/Payments/Request_to_Pay/EBA_R2P/Clearing_Directory_(CA)/Misc/Working_with.htm) for more information on uploading routing file to the clearing directory.

The below table contains the clearing file attributes.

| Clearing Directory Upload | File Format | Time Span for Publish | Details loaded to the system |
| --- | --- | --- | --- |
| EBARTPDIR | RTF |  | - Direct participant BIC - Bank   name - Initiation date - End date - Status - Indirect participant BIC - Message type allowed |

The below table contains the reachability key fields and the condition when the reachability is considered successful.

| Reachability | Condition |
| --- | --- |
| EBARTP | - BIC (Reachability key) - Payment Channel (Reachability key) - Reachability type = D - Status = ENABLED |

The license code for the EBAR2P clearing directory is “CAPYEU”.

[Payment Order Product](#)

Temenos RtP solution for EBA R2P supports the following payment order products.

- Instant payment (INSTPAY)
- Non Instant payment (SEPACT)

Applicable payment order products for an RtP request are based on the payment instrument specified by the payee.

[Outward Request Processing](#)

The diagram below shows the flow of Outward Request Processing (RtP Initiation).



The table below describes the activities performed during Outward request processing.

| Activity | Description |
| --- | --- |
| Accept and Enrich | The system enriches the incoming request with account-related details |
| Validation | RtP validations such as account validation, mandatory field validations and reachability check are performed |
| Generate RtP Request | After successful validation, the system generates a pain.013 message |

[Inward Request Processing](#)

The diagram below shows the flow of Inward Request Processing (receiving RtP).



The table below describes the activities performed during Inward Request Processing.

| Activity | Description |
| --- | --- |
| Validation | The system performs the RtP validations such as account validation, mandatory field validations and payment order product |
| Acknowledgement to RtP service | Once the payer service provider receives and validates the inward pain.013, the payer service provider sends a confirmation response to the EBA R2P |
| Park for payer consent | The system parks the received request for the payer action. |
| Send RtP response to requestor | After the payer responds to the RtP request, the system sends a pain.014 response to the payee service provider |
| EBA R2P | The central system then forwards the response to the payee service provider |
| Generate Payment request | If the payer agrees to pay the R2P request, the system sends the payment request to the payer service provider |
| Receive payment completion response | After the system settles the payment, it confirms the payment completion with the payer service provider |

[Cancellation](#)

The payee can request cancellation of previously sent payment requests before the payer bank processes the respective payment. The cancellation flow is supported only as part of the Approve later and Request to Pay Plus use cases. The Payee Service Provider sends the cancellation request to the R2P central system, which forwards it to the Payer Service Provider. The Payer Service Provider automatically processes and responds to the cancellation request with an approval or rejection response.

[Investigation](#)

The Payee Service Provider can investigate the status of the payment request if the response does not arrive in time. The EBA R2P central system receives the investigation message and forwards the investigation request to the Payer Service Provider, if required. The Payer Service Provider processes the investigation requests automatically and responds with the status of the payment request.

In addition to an investigation on status of the payment request, the Payee Service Provider can also send an investigation on status of the cancellation request. The EBA R2P central system replies to the investigation message based on the last status known to the clearing. In case, the clearing is not aware of the latest status, it can forward the investigation message to the Payer Service Provider to automatically process the investigation response based on the current status of payment request.

Read the [Introduction to Investigation](https://docs.temenos.com/docs/Solutions/Payments/Payments/RF/Request_to_Pay/RtP_Investigation/Introduction.htm#IntroductiontoInvestigation) section for more information on investigation.

In this topic

- [Introduction to EBA Request to Pay (R2P)](#IntroductiontoEBARequesttoPayR2P)




Copyright © 2020-2026 Temenos Headquarters SA

Cookie Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:33:09 PM IST
# Introduction to SWIFT MX Exceptions and Investigations

> Source: https://docs.temenos.com/docs/Solutions/Payments/International_Payments/PPSWEI/International_PaymentsCBPR/PPSWEI/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   SWIFT MX Exceptions and Investigations > Introduction

- SWIFT MX Exceptions and Investigations;)
  - [Introduction](../../International_PaymentsCBPR/PPSWEI/Introduction.htm)
  - [Configuration](../../International_PaymentsCBPR/PPSWEI/Configuration.htm)
  - [Working with](../../International_PaymentsCBPR/PPSWEI/Workingwith.htm)
  - [Tasks](../../International_PaymentsCBPR/PPSWEI/Tasks.htm)
  - [Outputs](../../International_PaymentsCBPR/PPSWEI/Outputs.htm)

Payments

# Introduction to SWIFT MX Exceptions and Investigations

Updated On 12 April 2026 |
 24 Min(s) read

Feedback
Summarize

SWIFT Investigation requests, response processing, and related messages are detailed in this section.

- Investigation Request – camt.110
- Investigation Response – camt.111
- Tracker Alert Notification – trck.003
- Tracker Investigation Status Notification – trck.005

## Message Types

The following table lists the messages supported by SWIFT MX Exceptions and Investigations.

| ISO 20022 message | Message Name | MT equivalent | Module code | Send (Outward) | Receive (Inward) | Forward (Redirect) |
| --- | --- | --- | --- | --- | --- | --- |
| camt.110 | Investigation Request | MT195, M295, MT199, MT299 | PPSWMX, PPSWEI |  |  |  |
| camt.111 | Investigation Response | MT196, MT296, MT199, MT299 | PPSWMX, PPSWEI |  |  |  |
| trck.003 | Tracker Alert Notification | NA | PPSWMX, PPSWEI |  |  |  |
| trck.005 | Tracker Investigation Status Notification | NA | PPSWMX, PPSWEI |  |  |  |

## Case Orchestrator

Case Orchestrator is a central investigation orchestration utility provided by Swift, enabling all Swift institutions to raise and respond to investigations. This central utility applies orchestration of investigations based on agreed industry business rules.

## Investigation Request

The Investigation Request message is sent by an agent to the Case Orchestrator to create an investigation or request a status update, or close an open investigation. SWIFT uses camt.110 ISO message type for an Investigation request.

[Investigation Type & Underlying Message Types](#)

Identifies the type of Investigation in coded form, and SWIFT supports only the following Investigation Types in Release 1. The table below provides the supported investigation requests and underlying original messages for which Investigation requests can be initiated.

| Investigation Request Initiated | Supported Message Types |
| --- | --- |
| Creditor Claim Non-Receipt (CCNR) | pacs.008, pacs.008 STP, pacs.009, pacs.009 ADV, MT103, MT202. |
| Cover Creditor Claim Cover Non-Receipt (CONR) | pacs.009 COV, MT202 COV |
| Unable To Apply By Creditor (UTAP) | pacs.008, pacs.008 STP, pacs.009, pacs.009 ADV, MT103, MT202, camt.052, camt.053, camt.054 |
| Request For Information (RQFI) | pacs.008, pacs.008 STP, pacs.009, pacs.009 ADV, pacs.009 COV, MT103, MT202, MT202 COV |

For SANC and COMP investigations, PPSWEI supports initiation across a wide range of payment statuses, including scenarios where the underlying payment is already completed (999 status).

[Investigation Sub Type](#)

Identifies the sub type of Investigation in coded form. The Unable To Execute (UTEX) investigation subtype is supported in Release 1, and it can be used when the Investigation type is RQFI.

For the Investigation Type RQFI, the following additional Investigation SubTypes are supported:

- **SANC** – Sanctions related investigation.
- **COMP** - Compliance related investigation subtypes.
  - FWTR - Funds/Wire Transfer Regulation
  - FRAD - Fraud
  - AMLI - Anti Money Laundering
  - FCCI – Financial Crimes Compliance

These SubTypes support the new investigation flows defined for the Sanctions (SANC) and Compliance (COMP) categories.

[Underlying Instrument Code](#)

Specifies the instrument or product to which the investigation refers. It is ISO 4-character code from the ISO 20022 ExternalInvestigationInstrumentCode list. For example, XBCT (Cross Border Credit Transfer), STAT (Statement Entry), and so on.

[Service Level Code](#)

Specifies a pre-agreed service or level of service between the Investigation Requestor and Responder. It is ISO 4-character code from the ISO 20022 ExternalInvestigationServiceLevel Code list. For example, RespondWithinOneBusinessDay (R01D), RespondWithinThreeBusinessDays (R03D), and so on.

[Investigation Data](#)

Investigation Data provides the required data, like investigation reason, reason subtype, depending on the Investigation Type for the responder to investigate. The table below describes the investigation data.

| Data | Description | Example |
| --- | --- | --- |
| Investigation Reason Code | Identifies the reason for the Investigation in coded form. It is ISO 4-character code from the ISO 20022 externalised InvestigationReasonCode list. | ISDT (The interbank settlement date is incorrect), DTAG (Further information pertaining to the debtor agent is requested), PURP (Further information pertaining to the purpose is requested). |
| Reason Sub Type Code | Further identifies the reason for the Investigation in coded form, it is ISO 4-character code from the ISO 20022 externalised InvestigationReasonSubType1Code list. | Mismatch NameAndAccount (MMNA ), Request Full Postal Address (RQPA), and Request Full Name (RQNM). |
| Additional Request Data | Provides additional information about the request in the narrative form. | - |

Read [Configuring SWIFT MX Exceptions and Investigations](../../../../International_Payments/PPSWEI/International_PaymentsCBPR/PPSWEI/Configuration.htm) section for more information.

## Processing and Responding to Inward Investigation Requests

This section explains how to process the Inward Investigation request message (camt.110) and provide Investigation responses (camt.111) for the request. Case Orchestrator forwards the request to the appropriate investigation responder.

[Duplicate Check on Inward Investigation Request](#)

The system validates if the investigation request with the same investigation type for the underlying payment is already received by comparing the details received in the inward investigation request with the existing investigation request case records present in the system. The system performs the duplicate check with the following default criteria.

- Original UETR Reference
- Original Message Identification
- Original Message Type
- Investigation Type code
- Case Type as IV
- Direction of the Investigation record

The system considers an incoming investigation request as a duplicate when,

- it matches the above criteria and
- the investigation type code is equal to CCNR or CONR or UTAP and
- the existing case is in 'Open' or 'Pending' status.

When the investigation request received is identified as duplicate, then:

If the automatic response is enabled, then the system sends an investigation response as follows:

- Investigation Status - RJCT (Rejected)
- Investigation Status Reason code - DU01 (Duplicate)
- Investigation Case Status - INVSTREJECTED

If the automatic response is not enabled, then the investigation request is parked in the manual queue for the user action, and the system marks the status of the Investigation case as INWORK with error reason as 'Investigation Request is duplicate of <Investigation Case Id>'. Below is the process flow diagram of processing and responding to Inward Investigation requests.



[Identification of Original Transaction](#)

TPH identifies the original transaction for which the investigation request is received using Unique End to End Reference (UETR) and/or original message name identification, and original message identification.

[Original Transaction not Found](#)

If the original transaction is not located in both the live and archived database, then the Investigation request is parked in the manual queue for the user action. The system marks the status of the Investigation case as 'INWORK' with error reason as 'Original Txn not found'.

[Original Transaction Already Returned](#)

If the status of the original transaction is Returned, then the system either sends an automatic negative response or the request is actioned manually by the bank user based on the configuration.

- If the automatic response is enabled, then the system sends an Investigation response as follows:
  - Investigation Status - RJCT
  - Investigation Status Reason code - ARDT (Already Returned).
  - Investigation case status - INVSTREJECTED.
- If the automatic response is not enabled, then the Investigation request is parked in the manual queue for the user action. The system marks the status of the Investigation case as 'INWORK' with error reason as 'Original Txn Already Returned'.

[Original Transaction is Already Rejected/Cancelled/Reversed](#)

If the status of the transaction is Rejected/Cancelled/Reversed, then the system either sends an automatic negative response or the request is actioned manually by the bank user based on the configuration.

- If the automatic response is enabled, then the system sends an Investigation response as follows:
  - Investigation Status - RJCT
  - Investigation Status Reason code - ARJT (Already Rejected).
  - Investigation case status is marked as INVSTREJECTED.
- If the automatic response is not enabled, then the Investigation request is parked in the manual queue for the user action. The system marks the status of the Investigation case as 'INWORK' with error reason as 'Original Txn Already Rejected/Cancelled/Reversed'.

[Original Transaction found](#)

If the original transaction is found based on the matching criteria and same is not in Returned/Rejected/Cancelled/Reversed status, then investigation request is parked in the manual queue for the user action and system creates a new case in the case management system with case status as INWORK.

If the Underlying Instrument code is STAT (Statement Entry), then original transaction identification is skipped, and investigation request is parked in the manual queue for the user action. The system creates a new case in the case management system with Case Status as 'INWORK'.

The user can view and action the Inward Investigation requests requiring manual action from the below enquiry.

| Enquiry Purpose | Enquiry Details |
| --- | --- |
| View Inward Investigation Request requiring manual action | Navigate to **User Menu** > **Payments** > **Payment Hub** **> Investigations & Cancellations** > **Investigations** > **Exceptions & Investigations** > **Inward Investigations** > **Inward Investigation Req – Require Manual Action**. |

[Request Investigation Status - Escalation Status **Reminders**](#)

Investigation requestor sends reminders (camt.110) through case orchestrator until the final investigation response (that is, camt.111 with Closed or Rejected status) is sent. Temenos Payments Hub (TPH) supports receipt, storing and viewing of such reminders from the inward investigations enquiries and user should can view the reminder count from enquiry listing screens. The investigation case status remains as INWORK.

[Request Investigation Status - Automated Status Reminders](#)

Case Orchestrator sends reminders (camt.110) until the final investigation response (that is, camt.111 with Closed or Rejected status) is sent. TPH supports receipt, storing and viewing of such reminders from the inward investigations enquiries and user can view the reminder count from enquiry listing screens. The investigation case status remains as INWORK.

The value of *Request Originator* field is Tracker BIC, that is TRCKCHZZ in case of automated status reminders.

[Request Investigation Closure](#)

Investigation requestor sends closure request (camt.110) through case orchestrator for open investigation request until the final investigation response (that is, camt.111 with Closed or Rejected status) is sent. TPH supports receipt, storing and closes investigation case based on the closure request. The case status is updated as INVESTIGATED. The users can view closed investigation requests from the View Investigation Request Queue.

[Sending an Investigation Response to Inward Investigation Request](#)

The investigation response message is sent by an agent to the Case Orchestrator to provide a response or status update on an investigation. Case Orchestrator forwards the response to the investigation requestor. The camt.111 is the ISO message type used by SWIFT for investigation response.

[Investigation Status](#)

It provides the status of investigation response in coded form. It is an ISO 4-character code from the ISO 20022 ExternalInvestigationStatusCode list. For example, CLSD (InvestigationClosed), PDNG(InvestigationPending), RJCT(InvestigationRejected).

[Investigation Status Reason Code](#)

It provides the reason for the investigation status in coded form. It is an ISO 4-character code from the ISO 20022 ExternalInvestigationStatusReasonCode list. For example, DU01(DuplicateRequest), INPO(InProgress), NOAD(NoAdditionalInformationAvailable).

[Investigation Status Reason proprietary](#)

It provides the reason for the investigation status in proprietary form.

[Response Data](#)

In case of a positive response, the responder must capture the data related to the investigation response under this data element. The table below describes the response data in detail.

| Response Data | Description | Example |
| --- | --- | --- |
| Confirmation | Confirms with details that a payment has successfully credited on an account | Confirmation of the payment booking. |
| Transaction Status | Provides the status of a payment in coded form when the booking is not done. It is an ISO 4-character code from the ISO 20022 External Payment Transaction Status Code list. | ACFC (AcceptedFundsChecked), BLCK(Blocked). |
| Transaction Status Reason | Provides the status of a payment in coded form. It is an ISO 4-character code from the ISO 20022 External Payment Transaction Status Code list. | AC06 (BlockedAccount), CUST(RequestedByCustomer). |
| Transaction Status Reason Additional Information | Provides further details on the status reason. | - |
| Transaction data | Provides transaction data. | Agent, or Amount or Any BIC or BIC FI or Cash Account or Code or Date or Date Time or Party or Remittance. |
| Response Narrative | Provides response in narrative form. | - |

The user can view and action the Inward Investigation requests requiring manual action from the below enquiry.

**User Menu** > **Payments** > **Payment Hub** > **Investigations & Cancellations** > **Investigations** > **Exceptions & Investigations** > **Inward Investigations** > **Inward Investigation Req – Require Manual Action**.

[](#)[Related Investigation Data (Applicable for SANC and COMP SubTypes)](#)

For Investigation Type RQFI with subtypes SANC, FWTR, FRAD, AMLI, and FCCI, an additional response block called Related Investigation Data is available. This block is used to capture any previous investigation details and supporting contact/location information required by the Case Orchestrator.

- Investigation Identification – Indicates the free text identifier (1–35 alphanumeric).
- Method – Indicates the delivery method. Allowed values include EDIC, EMAL, FAXI, POST, SMSM, and URID.
- Electronic Address – Indicates the email or other address (1–2048 characters).
- Location Details – Indicates the free text description.
- Postal Address (Structured) – Includes the following:
  - Name (1–140 chars)
  - Address Type (ADDR, PBOX, HOME, BIZZ, MLTO, DLVY)
  - Department
  - Street Name
  - Building Name
  - Floor
  - Town Name
  - Country
  - Up to 7 Address Lines

[Responding to Investigation Request](#)

The Investigation responder sends Investigation Response using one of the following statuses in the table below.

| Investigation Status | Description |
| --- | --- |
| CLSD | Investigation Closed |
| PDNG | Investigation Pending |
| RJCT | Investigation Reject |

- If Investigation Status = CLSD,
  - The investigation responder can optionally respond with investigation status reason code or investigation status reason proprietary.
  - The investigation status reason code is equal to INIT then response data is mandatory.
  - The investigation status reason is not provided, then response data is mandatory.
- If Investigation Status = PDNG or RJCT then Investigation Status Reason code or Investigation Status Reason proprietary is mandatory.

[Responding to CCNR/CONR Investigation Request](#)

The confirmation details or transaction status are sent as part of the response data when there is no investigation status reason, and Investigation Status = CLSD.

- If the payment is in a successfully processed status, then the system confirms the same.
- If the payment is in not successfully processed status, then Transaction Status is provided, and optionally user can provide Transaction Status Reason and Transaction Status Reason Additional Information.

[Responding to UTAP Investigation Request](#)

The transaction remittance details or response narrative are sent as part of the response data when there is no investigation status reason, and Investigation Status = CLSD.

[Responding to RQFI\_UTEX Investigation Request](#)

The transaction data (Agent, or Amount or Any BIC or BIC FI or Cash Account or Code or Date or Date Time or Party or Remittance) or response narrative are sent as part of the response data when there is no investigation status reason, and Investigation Status = CLSD.

[Authorising Investigation Response](#)

The user can authorise the investigation response from the user menu below:

**User Menu** > **Payments** > **Payment Hub** > **Payment Approvals Investigation & Cancellation - Auth** > **Payment Investigations Authorise Exceptions & Investigations** > **Authorise Inward Investigation**.

Upon successful authorisation, the Investigation response message is sent out to the SWIFT network, the system updates the status of the Investigation case as INVESTIGATED (CLSD response), INVSTREJECTED (RJCT response), and remains INWORK (PDNG response).

## Forwarding the Investigation Request

On receiving an inward Investigation Request for a redirected payment, the user reviews and forwards the received Investigation Request to the previous agent/next agent (the sender or receiver of the original payment leg) from the user menu below, and updates the case status as INVSTFWD once the investigation message is successfully forwarded.

**User Menu** > **Payments** > **Payment Hub** > **Investigations & Cancellations** > **Investigations** > **Exceptions & Investigations** > **Inward Investigations** > **Inward Investigation Req – Require Manual Action** and click the 'Forward the Inv Req' icon.

[Auto Forwarding the Investigation Response](#)

On receiving an investigation response for the forwarded investigation request, the system auto forwards the response to the case orchestrator and updates the investigation case status as follows,

- INVESTIGATED when the Investigation response status = CLSD.
- Remains unchanged as INVSTFWD when Investigation response status = PDNG.
- INVSTREJECTED when Investigation response status = RJCT.

## Viewing Investigation Response Sent

The user can view the details of the investigation response sent or response message forwarded from the menus below.

**User Menu** > **Payments** > **Payment Hub** > **Investigations & Cancellations** > **Investigations** > **Exceptions & Investigations** > **Inward Investigations** > **View Investigation Request**.

**User Menu** > **Payments** > **Payment Hub** > **Payment Inquiries** > **Pending and Processed Payments** > **Payments Enquiry - Transaction Wise** > **View in Detail** > **Investigation Message**.

## Tracker Alert Notification (trck.003)

On top of SWIFT network message validation, the Tracker applies additional checks to ensure the investigation response is valid. The trck.003.001.02 is tracker alert notification sent by the tracker to notify users of errors and warnings that may occur during message processing.

If a trck.003 is received for the investigation response sent or investigation request forwarded, the system updates the status of the Investigation case as 'TRACKERREJECTED' and the user can view (Rejection reason), action, or change the previously sent response and submit the investigation response again from the below menu.

**Inward Investigation**

**User Menu** > **Payments** > **Payment Hub** > **Investigations & Cancellations** > **Investigations** > **Exceptions & Investigations** > **Inward Investigations** > **Inward Investigation Req – Require Manual Action**.

## Initiating an Outward Investigation Request and Receiving Investigation Response

This section explains the creation of the Outward Investigation request message (camt.110) to the Investigation Responder through Case Orchestrator, receipt, storing, and viewing the Investigation responses (camt.111). The investigation request uses camt.110 ISO message type. Read [Investigation Request](#Investigation_Request) for more information. The user can initiate investigation request from the below user menu.

**User Menu** > **Payments** > **Payment Hub** > **Investigations & Cancellations** > **Investigations** > **Exceptions & Investigations** > **Outward Investigations** > **Send Investigation Request**.

The system does not support creating investigation requests using APIs.

[Creating Investigation Request for a Cross Border Credit Transfer (XBCT) Payment](#)

The Investigation Request is initiated for the credit transfer payment. Read [Working with](../../../PPSWEI/International_PaymentsCBPR/PPSWEI/Workingwith.htm#XBCT_Payment) section for more information on creating investigation request.

[Creating Investigation Request for a Statement Message (STAT)](#)

Read [Working with](../../../PPSWEI/International_PaymentsCBPR/PPSWEI/Workingwith.htm#STAT) section for more information on initiating an investigation request for a statement message.

[Sending Reminders and Closures](#)

User can initiate reminder (Request Investigation Status) and closures (Request Investigation Closure) until the final investigation response (camt.111 with Closed or Rejected status) is received. Read [Working with](../../../PPSWEI/International_PaymentsCBPR/PPSWEI/Workingwith.htm#Sending__Reminders_and_Closures) section for more information on sending reminders and closures.

[Authorising Investigation Requests](#)

The user can authorise the investigation request from the user menu below:

**User Menu** > **Payments** > **Payment Hub** > **Payment Approvals Investigation & Cancellation - Auth** > **Payment Investigations Authorise Exceptions & Investigations** > **Authorise Outward Investigation**.

Upon successful authorisation, the investigation request message is sent out to the SWIFT network and the status of investigation case record is updated to INVSTSENT or remains in INVSTSENT status (For Reminder request is sent) or INVESTIGATED status (Closure request is sent).

[Tracker Alert Notification (trck.003)](#)

If a trck.003 is received for the investigation request sent, the status of the investigation case is updated as 'TRACKERREJECTED' and user can view (Rejection reason), action or change details in the previously sent investigation request by clicking on Resend Investigation action and submit request again from the below menu.

**Outward Investigation**

**User Menu** > **Payments** > **Payment Hub** > **Investigations & Cancellations** > **Investigations** > **Exceptions & Investigations** > **Outward Investigations** > **Outward Investigation Request - Pending Final Response**.

If the trck.003 is received for the Reminder or Closure (camt.110) requests sent, then user should use 'Request Status (Reminder)' or 'Request Closure' actions from the dropdown menu instead of the 'Resend Investigation' action.

## Tracker Investigation Status Notification (trck.005)

The Case Orchestrator sends a tracker Investigation Status Notification (trck.005) message to a party involved in the business transaction, that is the REQUESTOR, to report on the status of an Investigation Request they have sent. Case Orchestrator generates the following status updates given in the table below.

| Status update | Description |
| --- | --- |
| ASGN | Assigns the responder for the investigation request and make the request available to the responder. |
| DTRP | Delivers to the responder. For the initial release, this status is generated at the same time as the ASGN status. In a future release, it reflects the delivery time to the receiver. |
| ERMD | Assigns the received escalated status reminder (request with action type RQST) to the responder and make the request available to the responder. |
| ARMD | Assigns the generated automated status reminder (request with action type RQST) to the responder and make the request available to the responder. |

The user can view the Tracker Investigation Status Notification (trck.005) message from the user menu below:

**User Menu** > **Payments** > **Payment Hub** > **Investigations & Cancellations** > **Investigations** > **Exceptions & Investigations** > **Outward Investigations** > **View Investigation Request**.

## Manually Closing Investigation Request and Forwarded Investigation Messages

Read [Working with](../../../PPSWEI/International_PaymentsCBPR/PPSWEI/Workingwith.htm#Manually_Closing) section for more information on manually closing th request.

## Receipt and Storing of Investigation Response

The Investigation Responder would respond to the Investigation Request, and the Case Orchestrator forwards the Response to the Investigation Requestor. The camt.111 ISO message type used by SWIFT for Investigation response.

The investigation responder sends a response using one of the following statuses.

| Investigation Status | Description |
| --- | --- |
| CLSD | Closed by the responder after providing the necessary information to the initiated query. |
| PDNG | An intermediary status to the requestor, with a clear indication of the pending status. Therefore, associated with that status, the investigation status reason Code is mandatory. |
| RJCT | Rejected by the responder. Associated with that status, the investigation status reason code is mandatory and provides context on the reject status. |

[Updating Investigation Case Status based on the Response](#)

The case management record status is updated as given below for the following responses,

- CLSD - Case Management record status is updated as INVESTIGATED
- PDNG - Case Management record status remains unchanged as INVSTSENT
- RJCT - Case Management record status is updated as INVSTREJECTED

User can view the investigation response message in XML format from the below menus.

- **User Menu** > **Payments** > **Payment Hub** > **Investigations & Cancellations** > **Investigations** > **Exceptions & Investigations** > **Outward Investigations** > **View Investigation Request**.
- **User Menu** > **Payments** > **Payment Hub** > **Payment Inquiries** > **Pending and Processed Payments** > **Payments Enquiry - Transaction wises** > **View in Detail** > **Investigation Message**.

In this topic

- [Introduction to SWIFT MX Exceptions and Investigations](#IntroductiontoSWIFTMXExceptionsandInvestigations)

- [Message Types](#MessageTypes)
- [Case Orchestrator](#CaseOrchestrator)
- [Investigation Request](#InvestigationRequest)
- [Processing and Responding to Inward Investigation Requests](#ProcessingandRespondingtoInwardInvestigationRequests)
- [Forwarding the Investigation Request](#ForwardingtheInvestigationRequest)
- [Viewing Investigation Response Sent](#ViewingInvestigationResponseSent)
- [Tracker Alert Notification (trck.003)](#TrackerAlertNotificationtrck003)
- [Initiating an Outward Investigation Request and Receiving Investigation Response](#InitiatinganOutwardInvestigationRequestandReceivingInvestigationResponse)
- [Tracker Investigation Status Notification (trck.005)](#TrackerInvestigationStatusNotificationtrck005)
- [Manually Closing Investigation Request and Forwarded Investigation Messages](#ManuallyClosingInvestigationRequestandForwardedInvestigationMessages)
- [Receipt and Storing of Investigation Response](#ReceiptandStoringofInvestigationResponse)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 6:02:14 PM IST
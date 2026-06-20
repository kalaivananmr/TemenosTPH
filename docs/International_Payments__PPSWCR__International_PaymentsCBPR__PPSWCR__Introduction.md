# Introduction to SWIFT MX Cancellations and ROI

> Source: https://docs.temenos.com/docs/Solutions/Payments/International_Payments/PPSWCR/International_PaymentsCBPR/PPSWCR/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   SWIFT MX Cancellations and ROI > Introduction

- SWIFT MX Cancellations and ROI;)
  - [Introduction](../../International_PaymentsCBPR/PPSWCR/Introduction.htm)
  - [Configuration](../../International_PaymentsCBPR/PPSWCR/Configuration.htm)
  - [Working with](../../International_PaymentsCBPR/PPSWCR/WorkingWith.htm)
  - [Tasks](../../International_PaymentsCBPR/PPSWCR/Tasks.htm)
  - [Outputs](../../International_PaymentsCBPR/PPSWCR/Tasks.htm)

Payments

# Introduction to SWIFT MX Cancellations and ROI

Updated On 12 April 2026 |
 113 Min(s) read

Feedback
Summarize

The CBPR+ (Cross-Border Payments and Reporting Plus) working group is responsible for defining the MX message formats and usage guidelines (available in SWIFT CBPR+ portal).

Temenos Payments Hub support processing of cross border international payments using SWIFT MX (ISO20022) messages.

This document explains about the processing of FI-to-FI cancellation request and its responses and also the customer cancellation request and its responses.

- FI to FI Payment Cancellation Request and responses (Inward and Outward)  – Camt.056 and camt.029/Pacs.004/Pacs.002
- Customer Payment Cancellation Request – Camt.055, Camt.056 and Camt.029/Pacs.004

## Message Types

The following table lists the SWIFT CBPR+ messages supported by Temenos Payments Hub system for Cancellations and Resolution of Investigations. Read [SWIFT MX](../../../PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm) for more information.

| ISO20022 MX Message | Message Type | MT Equivalent | Module Code | Outward | Inward | Redirect | Business Service |
| --- | --- | --- | --- | --- | --- | --- | --- |
| camt.056.001.08 | Payment Cancellation Request | MT192 | PPSWMX  PPSWCR |  |  | × | swift.cbprplus.02 |
| camt.029.001.09 | Resolution of Investigation | MT196 | PPSWMX  PPSWCR |  |  |  | swift.cbprplus.02 |
| Camt.055.001.08 | Customer Payment Cancellation Request | - | PPSWMX  PPSWCR | × |  | × | swift.cbprplus.01 |
| Camt.058.001.08 | Notification To Receive Cancellation Advice | - | PPSWMX PPSWCR |  | × | × | swift.cbprplus.02 |

## Payment Cancellation Processing

Cancellation request message is the recall message that can be initiated by the customer or bank to recall the already sent payment transfer. The Assigner (who sends the cancel request message) sends this message to the Case Assignee (who receives the cancel request message) to request the cancelation of a payment previously sent.

Cancellation request can be sent for the following CBPR+ outgoing payment messages:

- Payments sent using serial method
  - Serial Customer Transfer (pacs.008 or MT103)
  - Serial Bank Transfer (pacs.009 or MT202)
- Payment sent using cover method
  - Direct Message
    - Announcement of Customer Transfer (pacs.008 or MT103), when payment is settled through cover method
    - Announcement of Bank Transfer (Pre-Advice of Bank Transfer - pacs.009 ADV or MT202), when payment is settled through cover
  - Cover message
    - pacs.009 COV or MT202 COV cover against the Customer Transfer announcement (pacs.008 or MT103 ), when payment is settled through cover
    - pacs.009 or MT202 COV for the Bank Transfer (pacs.009 ADV or MT202), when payment is settled through cover

The Agent sends the FI to FI Payment Cancelation Request message to request the cancelation of a payment previously sent. The message is sent either,

- directly to the Agent or through the SWIFT Community CASE solution, or
- serially through other agents.

Temenos Payments Hub does not support directly to an agent or through the SWIFT Community CASE solution.

Temenos Payments Hub bank may receive the inward cancellation request from other bank to recall the incoming payment that is being processed or already been credited. For cross border international payments, CBPR+ camt.056 message is used. The equivalent message in SWIFT FIN is MT192.

The Resolution of Investigation message camt.029 is the response message for the Cancel request sent by the case assignee to the assigner. This message is used to inform the resolution of a case, and optionally provide details about the corrective action undertaken by the case assignee and the information on the return, if applicable.

For CBPR+ international payments, camt.029 message is generated for positive, interim, and negative action. In camt.029 message, the possible status codes to specify the status of the cancellation request’s investigation are:

| Status Code | Description |
| --- | --- |
| CNCL | The payment has been cancelled as requested. This status concludes the investigation, whereby a Payment Return may follow, if funds need to be returned. |
| PDCR | The Investigation of the Payment Cancelation Request is pending that is under ongoing investigation to provide a final status confirmation. An additional Cancellation Status Reason Information should be provided to further clarify the status. For example, a Status Reason code RQDA can be used to indicate that the debit authority has be requested from the Creditor. |
| RJCR | The Payment Cancelation Request is rejected. A status concluding the investigation that must include additional Cancellation Status Reason Information to provide an explanation as to why the request was rejected. |

Following are the cancellation status reason codes in a camt.029 message:

| Code | Name | Definition | Use Case |
| --- | --- | --- | --- |
| AC04 | Closed Account Number | Account number specified has been  closed on the receiver’s books. | Complimenting a Reject Status. Payment Cancelation Request cannot be  accepted as the Creditor has closed their account. |
| AGNT | Agent Decision | Reported when the cancellation  cannot be accepted because of an  agent refuses to cancel | Complimenting a Reject Status. Payment Cancelation Request cannot be  accepted as an Agent in the payment transaction does not accept the  request. |
| AM04 | Insufficient Funds | Amount of funds available to cover  specified message amount is  insufficient | Complimenting a Reject Status. Payment Cancelation Request cannot be  accepted as the Creditor has insufficient funds to perform the return payment. |
| ARDT | Already Returned | Cancellation not accepted as the  transaction has already been returned | Complimenting a Reject Status. Payment Cancelation Request cannot be  accepted as the payment already has return payment. |
| CUST | Customer Decision | Reported when the cancellation  cannot be accepted because of a  customer decision (Creditor). | Complimenting a Reject Status. Payment Cancelation Request cannot be  accepted as the Creditor does not provide authority to return the payment. That is  believe the payment was justified. |
| INDM | Indemnity Request | Indemnity is required before funds can  be returned | Complimenting a Pending or Reject Status. Payment Cancelation Request  cannot be accepted until an indemnity agreement is established. |
| LEGL | Legal Decision | Reported when the cancellation cannot be  accepted because of regulatory rules. | Complimenting a Reject Status. |
| NOAS | No Answer From  Customer | No response from beneficiary (to the cancellation  request). | Complimenting a Reject Status. Payment Cancelation Request  cannot be accepted as the Creditor has not responded to a  Debit Authority request to return the payment. |
| NOOR | No Original  Transaction  Received | Original transaction (subject to cancellation) never  received | Complimenting a Reject Status. Payment Cancelation Request  cannot be accepted as it is believed that the original payment  was never received for the UETR and references provided. |
| PTNA | Passed To The  Next Agent | Reported when the cancellation request cannot be  accepted because the payment instruction has been  passed to the next agent. | Complimenting a Pending Status. Payment has been onward  processed to the next agent in the transaction. The Payment  Cancelation Request has therefore been forwarded to this Agent, a further resolution message is sent once this Agent  provides a response. |
| RQDA | Requesting Debit  Authority | Reported when authority is required by the Creditor to  return the payment | Complimenting a Pending Status. Payment has been credited  to the creditor, Authority to Debit the Creditor and return the  payment is being requested. A further resolution message is sent once the Creditor provides a response. |

Following sections explain the support for this message:

In addition to SWIFT MX licence, Temenos Payments Hub bank must also have PPSWCR licence to accept and send cancellation request, and resolution to investigation messages in ISO format from and to SWIFT. The bank requires this licence also to view the SWIFT ISO Cancellation requests and responses from the dedicated SWIFT ISO Cancellation Enquiry screens.

Support for unstructured address format ends with go-live of SWIFT SR2026. TPH restricts unstructured address format for parties and agent in as SWIFT will not accept CBPR+ payments with unstructured address elements only.

[Processing Inward Cancellation Request](#)

This section explains the processing of inward cancellation request message and its corresponding responses for the request.

[Duplicate Check for Inward Cancellation Request](#)

On receiving inward cancellation request camt.056, Temenos Payments Hub bank maps the message and performs duplicate check to verify whether there are any existing cancellation request received for the same payment. This check is performed using Unique End to End Reference and Original Message Identification. Performing duplicate check for the incoming cancellation request is configurable at the Message Mapping Parameter table and it can be changed by the bank user, if required.

On performing duplicate check, if there is already a cancellation request received for the same payment, then Temenos Payments Hub checks for the status of the cancellation request.

- If the status is Rejected, Temenos Payments Hub maps the received camt.056 with the payment and the cancellation request is available for the user to take action in manual queue.
- If the status is Pending and the user has not taken any action on the existing cancellation request, then the Temenos Payments Hub bank maps the received camt.056 as an ignored message and only the existing cancellation request is available for the user to take action.
- If the status is already Accepted, then Temenos Payments Hub bank automatically rejects the cancellation request by sending out negative Resolution of Investigation message camt.029 with RJCR status code and ARDT reason code irrespective of the configuration in the Clearing Setting table for the SWIFT network. UETR and Transaction reference of the already returned payment is displayed in the *Additional Information* field.

While sending out the camt.029 message to the assigner of the cancellation request, the bank always checks for RMA. Only if RMA is present, the system sends out the camt.029 message, else parks the cancellation record in the manual queue with the error message. The user has to manually create an RMA configuration with the Temenos Payments Hub bank and the assigner of the cancellation request, and send the camt.029 message.

[Identifying Original Transaction](#)

Once duplicate check is complete, Temenos Payments Hub identifies the original transaction for which the cancellation request is received using Unique End to End Reference (UETR) and Original Message Identification. If the system finds more than one transaction using UETR (in case of direct and cover messages), the system compares the original message identification to fetch the transaction.

If there is no UETR in the received cancellation request message, the system uses the following parameters to identify the original transaction:

- Compare the Original Instruction Identification tag in the XML with the FT number
- Original Interbank Settlement Date
- Amount

If API is configured in the Message Mapping Parameter table, the criteria given in the API is given preference to find the original transaction.

Once the transaction is identified, there is no requirement from SWIFT to check the number of allowed days within which the cancellation request must be received for the payment. So, the corresponding configuration for allowed days of cancellation request in the Clearing Setting table is configured as BLANK. Hence, the system does not have to perform any validation regarding the number of allowed days.

If the original transaction is not found, Temenos Payments Hub bank checks for the configuration in the Clearing Setting table whether to send out an automatic negative response for the cancellation request or not. If the configuration is set to be automatic, then Temenos Payments Hub generates camt.029 message with RJCR status code and NOOR reason code and send out to the assigner of the cancellation request. If the configuration is set to be manual, then the system parks the cancellation request message for manual action with status as Unmatched.

[Enquiries for Inward SWIFT Cancellation Request](#)

The following sections describe the enquires used to view and perform actions on the inward SWIFT cancellation requests.

[Inward Cancellation Request – Manual Action](#)

Temenos Payments Hub parks all the incoming cancellation request camt.056 for user action in the **Inward Cancellation req – Require manual action** enquiry. This enquiry holds the following:

- The matched ISO incoming cancellation requests from SWIFT that requires manual action.
- The cancellation requests that are not matched with original transaction
- The cancellation requests for which the responses got rejected by SWIFT network.

To access all these menus and enquiries, the bank requires PPSWCR license in addition with PPSWMX license.

This enquiry is accessible through the **User Menu** > **Payments** > **Payments Hub** > **Investigations & Cancellations** > **Cancellations** > **SWIFT ISO Cancellations** > **Inward Cancellation Req- Require Manual action** menu.

From this enquiry, the user can accept, reject or send pending response for the cancellation request. It is also possible that the user can send pending response first and then send final response such as Accept or Reject. So, for single cancellation request, it is possible to have multiple Resolution to Investigation messages (camt.029).

Similarly, in case of duplicate request, it is possible to have multiple camt.056 for the same transaction. In such cases, the user can view all the received incoming camt.056 and all the outward camt.029 responses from the [Pending and Processed](#Pending_and_Processed_Enquiry) enquiry and in the **Inward Cancellation Req- Require Manual action** enquiry using the View buttons. The possible user actions from this enquiry are given below.

| Icon | Name | Description |
| --- | --- | --- |
|  | View EBQA Details | Allows to view the EBQA details |
|  | Amend EBQA | Allows to edit the EBQA details to respond to camt.056 |
|  | View Orig Txn | Allows to view the original transaction for which the cancellation request is received |
|  | View Cancel Req | Allows to view all the incoming camt.056 messages received for that particular transaction |
|  | View ROI | Allows to view all the outgoing camt.029 messages sent for that particular cancellation request |

While responding to the cancellation request, the user can select the originator details for the response in the *Resp Originated By* field. The allowed values are:

- Customer - Indicates that the customer or beneficiary of the original transaction is the originator for the response of the cancellation request.
- Bank - Indicates that the processing company is the originator for the response of the cancellation request.
- Blank - This is the default value. The company BIC gets mapped in the outgoing message when this value is selected.

When the user rejects the cancellation request using the CUST reject reason code, and if the *Resp Originated By* field is set as Bank, the system generates the 'Response originator is not applicable for this reason code' error. The user must change the response originator as Customer and submit the record.

If the Temenos Payments Hub processing bank is not MX enabled and receives the cancellation request camt.056 for the incoming transaction, the user is not allowed to take any action from this manual action enquiry. If the user tries to perform any action on the cancellation request, the system displays the “Action not allowed since the company is MT enabled” error message. The user can respond for this cancellation request with MT199 (Free Format Message) only and not with MT196 (Answers). The user can create a Free Format Message from the Send Free Format Message enquiry (**User Menu** > **Payments** > **Payment Hub** > **Investigations** > **Investigations – Free Format Msgs** > **Send Free Format Message**).

[Inward Cancellation Request – View Status](#)

The user can view the status of all incoming cancellation requests in the **Inward Cancellation Request – View Status** enquiry. Along with the status, the user can also view all the received camt.056 and the outward camt.029 messages.

To access this enquiry, go to **User Menu** > **Payments** > **Payments Hub** > **Investigations & Cancellations** > **Cancellations** > **SWIFT ISO Cancellations** > **Inward Cancelation Request – View Status**.

To access the menus and enquires, the bank requires the PPSWCR license in addition to the PPSWMX license.

| Icon | Name | Description |
| --- | --- | --- |
|  | View EBQA Details | Allows to view the EBQA details |
|  | View Orig Txn | Allows to view the original transaction for which the cancellation request is received |
|  | View Cancel Req | Allows to view all the incoming camt.056 messages received for that particular transaction |
|  | View ROI | Allows to view all the outgoing camt.029 messages sent for that particular cancellation request |

[](#)[Pending and Processed Enquiry](#)

To view the inward cancellation request messages,

1. Go to **User Menu > Payments > Payment Hub > Payment Inquiries > Pending and Processed Payments > Payments Enquiry – Transaction wise**.
2. Click  across the required payment from the enquiry list.
3. On the Payment Information window, select the View Inward Cancellation Request Message option from the drop-down and click .

The possible user actions from this enquiry are given below:

| Icon | Name | Description |
| --- | --- | --- |
|  | View EBQA Details | Allows to view the EBQA details |
|  | View Cancel Req | Allows to view all incoming camt.056 messages received for that particular transaction |
|  | View ROI | Allows to view all outgoing camt.029 messages sent for that particular cancellation request |

[Authorising Inward Cancellation Request](#)

Any changes made in the manual enquiry needs to be authorised by the second user. Once the user has made changes in the **Inward Cancellation Req- Require Manual action** enquiry, the record gets parked in the **Authorise Inward Cancellation Requests authorisation** enquiry for the second user’s approval.

To access the enquiry, go to **User Menu** > **Payments** > **Payments Hub** > **Investigations & Cancellations** > **Cancellations** > **SWIFT ISO Cancellations** > **Authorise Inward Cancellation Requests**.

The following icons enable the user to perform the appropriate actions:

| Icon | Name | Description |
| --- | --- | --- |
|  | View | Allows to view the underlying payment. |
|  | Auth EBQA | Allows to open the CBPR+ specific view and authorize EBQA screen (all fields in read only mode) and display the cancellation request details. The user can authorise the record using this version. |
|  | Reject EBQA | Allows to open the CBPR+ specific view and authorize EBQA screen (all fields in read only mode) and display the cancellation request details. The user can reject the cancellation request using this version. So, the message gets displayed again in the I**nward Cancellation req – Require manual action** enquiry for manual action. |

[Enquiry for Investigation Users](#)

This enquiry displays all the incoming transactions that are received from the repair queue for which a cancellation request is received. Investigation users may not have access to all the menus and sub-menus. In that case, if the investigation users wants to take actions on the cancellation request, they can use this sub-menu through **User Menu** > **Payments** > **Payments Hub**> **Payment Investigation and Cancellations** > **Pending Repair txn-Cancel ReqRcvd**. The user must have the PP license to access this enquiry.

Refer to the [Investigations and Enquiries](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Investigations/Introduction.htm) guide for more information.

[Validations for Resolution of Investigation camt.029 Message](#)

When the incoming cancellation request is parked in the **Inward Cancellation Req- Require Manual Action** enquiry, there are three possible actions (Accept, Reject, and Pending) available for the user. For all these three actions, the system generates corresponding Resolution of Investigation (camt.029) message and sends to the assigner of the cancellation request.

When the user selects the Accept action for the cancellation request, the user must adhere to the below validations, otherwise the system generates an error message.

- For Accept action, the reason code is not required. If the reason code is selected, then the system displays an error message.
- The user can optionally enter the additional information in the *Accept Information* field. The user should not enter the additional information in the *Pending and Reject information* field.
- For the Accept action, if the user enters the additional information, then it should not exceed more than two lines and each line should not exceed more than 105 characters. Otherwise, the system generates an error message.

When the user selects the Pending action for the cancellation request, the user must adhere to the below validations:

- For the Pending action, the user must select the corresponding reason code.
- For the Pending action, the user must select only the corresponding Pending reason codes. If other reason codes are selected, the system displays an error message.
- The user can optionally enter the additional information in the *Pending Information* field. The user must not enter the additional information in the *Accept and Reject Information* field.
- For the Pending action, if the user enters the additional information, then it should not exceed more than two lines and each line should not exceed more than 105 characters. Otherwise, the system displays an error message.

When the user selects the Reject action for the cancellation request, the user must adhere to the below validations,

- For the Reject action, the user must select the corresponding reason code.
- For the Reject action, the user must select only the corresponding Reject reason codes. If other reason codes are selected, the system generates an error message.
- The user can optionally enter the additional information in the Reject Information field. The user must not enter the additional information in the Accept and Pending Information field.
- For the Reject action, if the user enters the additional information, then it should not exceed more than two lines and each line should not exceed more than 105 characters. Otherwise, the system generates an error message.
- For the Reject action, if the user selects ARDT (Already Returned) reason code for the cancellation request, then the user has to enter the return transaction reference in the Return Reject Reference field. If the user leaves this field blank, then the system displays an error message.
- For the Reject action, if the user selects ARDT (Already Returned) reason code for the cancellation request, then the user can enter the additional information in single line only. If the additional information exceeds more than one line, then the system displays an error message.

If reason code in resolution of investigation message is:

- PTNA - TPH validates to ensure that the user enters BIC of the next agent (BIC-8 and BIC-11) in line 1 of *Pending Additional Info* field. BIC is not validated.
- ARDT - Populates UETR of the original transactions in line 1 of *Reject Addl Info* field, followed by user entered details at the XSLT level.

Only if all the above validations are satisfied, the system generates the Resolution of Investigation (camt.029) message and sends to the assigner of the cancellation request.

[Receiving Inward Cancellation Request for Customer or Bank Transfer Payment Settled Serially and Customer or Creditor is Credited](#)

Temenos Payments Hub bank may receive the inward cancellation request for the payment that has already been credited to the customer or creditor serially. The applicable message types for this scenario are MT103/MT202 or pacs.008/pacs.009 or MT202 COV/pacs.009 COV.

In this case, the cancellation request is always processed manually. So the configuration in the Clearing Setting table for CBPR+ cancellation request is configured as ‘Manual’ always for automatic return option.

The cancellation request camt.056 message gets parked in the **Inward Cancellation Req- Require Manual action** enquiry for the user action.



The following are the possible user actions:

| Action | Description |
| --- | --- |
| Accept | When user accepts the cancellation request, the system validates the status of the credit account of the original transaction to ensure that the account is active to be debited for the return transaction amount. If the account is closed, then the user can only reject the cancellation request. If the account is active, then the system checks for RMA between Temenos Payments Hub bank and the instructing agent of the original transaction for sending pacs.004 message.   - If RMA is not present, the system displays an error message. The user has to manually create an RMA to proceed further. - If RMA is present, the system generates a return message (pacs.004) with reason code ‘FOCR’. - The system updates the status of the request to indicate that the request is accepted and return is in progress (RETURNINPROGRESS). - Once the return transaction is completed, the status of the original transaction is updated as ‘Completed with Return’. The system generates a positive Resolution of Investigation message (camt.029) with CNCL status code and sends to the assigner of the cancellation request. The status of the cancellation request is updated as ‘CANCELACCEPTED’. Then the return message Pacs.004 is emitted out. - If there are any errors in processing of the return message, the return transaction moves to repair status. The cancellation record status remains in RETURNINPROGRESS. The positive ROI message is not sent out. If the user cancels the transaction from repair queue, the system updates the cancellation record back to INWORK for manual action. - The system updates the Return transaction reference in the cancellation record. - The user can view the return transaction details from the **Pending and Processed** enquiry of the underlying credit transfer and vice versa. - The system updates the audit trail of the original transaction as ‘Inward cancellation request is accepted’ - It is possible for the bank to receive negative ACK or negative DLN for the pacs.004 message. Refer to the [Resubmission of Payment messages based on Technical Acknowledgement](../../../PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm#202107) section for more information on processing of negative ACK or negative DLN for pacs.004. |
| Reject | When the user rejects the cancellation request, camt.029 message gets generated with RJCR status code and the user selected reject reason code. The system updates the cancellation request status as Rejected. |
| Pending | When the user sends the pending response for the cancellation request, the system generates the camt.029 message with PDCR status code and user selected pending reason code. The cancellation request remains in the queue for manual action. |

[Receiving Inward Cancellation Request for Customer or Bank Transfer Payment Settled Serially and Customer or Creditor is not Credited](#)

Temenos Payments Hub bank may receive the inward cancellation request for,

- Payment that is being processed (not reached any final statuses)
- Payment that is in interim status such as Repair or
- Payment waiting for sanctions response or for any other response from the external system. The applicable message types for this scenario are MT103/MT202 or pacs.008/pacs.009 or MT202 COV/pacs.009 COV.

In this case, the system marks the payment as the cancellation request is received so that the payment is not processed completely and moves to the repair queue, if not already moved. The user can submit or release the payment from the repair queue only if the cancellation request is rejected. The system parks the cancellation message (camt.056) in the 'Inward Cancellation Req- Require Manual action' manual queue for user actions.

Here, there are two possible scenarios for the payment based on the settlement method.

- Payment in interim status that was settled by Instructing agent
- Payment in interim status that is yet to be settled by Instructed agent

For both the above scenarios, cancellation request is parked in the manual queue for user actions.



The following are possible user actions:

| Action | Description |
| --- | --- |
| Accept | When user accepts the cancellation request, the system checks for RMA between TPH bank and the assigner of the cancellation request for sending Camt.029 message. TPH also checks for RMA between TPH bank and the instructing agent of the original transaction for sending Pacs.004 message.   - If RMA is not present, the system generates an error message. The user has to manually create an RMA to proceed further. - If RMA is present, the system generates a return message (pacs.004) with ‘FOCR’ reason code. - The system updates the status of the request to indicate that the request is accepted and return is in progress (RETURNINPROGRESS). - Once the return transaction is completed, the system updates the status of the original transaction as 'Completed with Return'. The system generates a positive Resolution of Investigation message (camt.029) with CNCL status code and sends to the assigner of the cancellation request. The status of the cancellation request is updated as ‘CANCELACCEPTED’. Then the return message Pacs.004 is emitted out. - If there are any errors in processing of the return message, the return transaction moves to repair status. The cancellation record status remains in RETURNINPROGRESS. The positive ROI message is not sent out. If the user cancels the transaction from repair queue, the system updates the cancellation record back to INWORK for manual action. - The system updates the return transaction reference in the cancellation record. - The user can view the return transaction details from the **Pending and Processed** enquiry of the underlying credit transfer and vice versa. - The system updates the audit trail of the original transaction as ‘Inward Cancellation request is accepted’. - The bank can receive negative ACK or negative DLN for the pacs.004 message. Refer to the [Resubmission of Payment messages based on Technical Acknowledgement](../../../PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm#202107) section for move information on processing negative ACK or negative DLN for pacs.004.   When the user accepts the cancellation request for the payment that has been already settled by the Instructing Agent and if the transaction is in the Repair status due to debit party validation failure error, the system displays the “Cannot return the payment since the debit party is not determined for the original transaction” error on the screen. The user has to manually correct the error for the original transaction and submit from the repair queue. Once submitted, the transaction again falls in the Repair status since the cancellation request is received for the transaction. The user can perform actions for the cancellation request from the manual enquiry.  When the user accepts the cancellation request for the payment that is yet to be settled by the Instructed agent, the system checks for RMA between the Temenos Payments Hub bank and the assigner of the cancellation request for sending camt.029 message. Temenos Payments Hub also checks for RMA between its bank and the instructing agent of the original transaction for sending pacs.002 message.   - The system generates the camt.029 message and sends to the assigner of the cancellation request with CNCL status code and FOCR reason code. - The system sends the reject message (pacs.002) with ‘FOCR’ reason code to the instructing agent of the underlying payment. - Once the reject message is successfully sent, the system marks the underlying credit transfer as ‘rejected’ along with the reject reason code. - The system updates the cancellation record as Reject is sent for the transaction and updates the status as CANCELACCEPTED. The reason for accepting the record entered by the user in the *Accepted Reason* field is sent out in the *Additional Information* field in the camt.029 and pacs.002 messages. - The system updates the audit trail of the transaction as ‘Inward Cancellation request is accepted’. - The bank can receive negative ACK or negative DLN for the pacs.002 message. Refer to the [Processing of Non – Payment messages based on Technical Acknowledgement](../../../PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm#ProcessNonPayment) section for more information on processing of negative ACK or negative DLN for pacs.002. |
| Pending | When the user sends pending response for the cancellation request, the system generates the camt.029 message with PDCR status code and the cancellation request remains in the queue for manual action. The system updates the audit trail of the transaction as ‘Pending response is sent for the cancellation request’. |
| Reject | When the user rejects the cancellation request, the system generates the camt.029 message with RJCR status code and updates the cancellation request status as Rejected. The system updates the Audit trail of the transaction as 'Inward cancellation request is rejected'.  Before taking an action on the cancellation request, if the user tries to act on the transaction (such as Return or reject action) from interim status, then the system displays an error message as 'Recall Request has been received for this payment. Please take action so that return or reject gets triggered automatically'. Hence the user is restricted to take action for the transaction which has received cancellation request. |

[Receiving Inward Cancellation Request for Rejected, Reversed, and Cancelled Payments](#)

Temenos Payments Hub bank may receive inward cancellation request for the payment that has already been rejected, reversed, or cancelled. In such cases, Temenos Payments Hub automatically sends the negative Resolution of Investigation message (camt.029) with RJCR status and ARDT (Already Returned) reason codes to the assigner of the cancellation request.

After receiving the cancellation request and parking it in the manual queue, the user can move the payment to these above-mentioned statuses from the repair queue.

In such cases, the user can only reject the cancellation request from the manual queue and cannot perform any other actions, since the payment has already reached the final status. On rejecting the cancellation request and after authorisation, the system generates the camt.029 message with RJCR status and sends to the assigner of the cancellation request. The audit trail of the transaction is updated as ‘Inward cancellation request is rejected’.

If the user tries to accept or send pending action for such cancellation requests from the manual queue, then the system displays an error message, so the only option for the user is to reject this cancellation request.

[Receiving Inward Cancellation Request for Seized Payments](#)

Temenos Payments Hub bank may receive inward cancellation request for the payment that has already been seized. In such cases, Temenos Payments Hub automatically sends the negative Resolution of Investigation message (camt.029) with RJCR status and LEGL reason codes to the assigner of the cancellation request.

If RMA is not available between Temenos Payments Hub and the assigner of the cancellation request, the system parks the cancellation request in the manual queue and if the user tries to accept or send pending response for the cancellation request, then an error message is displayed for the user.

In such cases, the user can only reject the cancellation request from the manual queue. While rejecting the cancellation request from the manual queue, the user must select the reject reason code as LEGL. On rejecting the cancellation request and after authorisation, the system generates the camt.029 message with RJCR status code and sends to the assigner of the cancellation request. Audit trail of the transaction is updated as ‘Inward cancellation request is rejected’.

[Receiving Inward Cancellation Request for Returned Payments](#)

Temenos Payments Hub bank may receive inward cancellation request for the payment that has already been returned. In such case, Temenos Payments Hub automatically sends the negative Resolution of Investigation message (camt.029) with RJCR status and ARDT reason codes to the assigner of the cancellation request. The transaction reference of the returned payment is displayed in the Additional Information tag of the camt.029 message.

The user can return the payment manually from the repair queue after the cancellation request is received and parked in the manual enquiry.

In such cases, the user can only reject the cancellation request from the manual queue and cannot perform any other action, since the payment has already been returned. On rejecting the cancellation request, the system generates the camt.029 message with RJCR status and sends to the assigner of the cancellation request. While rejecting the cancellation request, the user must select the reject reason code as ARDT and enter the transaction reference of the return payment in *Return Reject Reference* field. The system updates the audit trail of the transaction as ’Inward cancellation request is rejected’.

If the user tries to accept or send pending action for such cancellation request from manual queue, the system displays an error message, so the only option for the user is to reject this cancellation request.

[Receiving Inward Cancellation Request for Payments Settled through Cover](#)

Temenos Payments Hub bank may receive inward cancellation request for the payment (pacs.008/MT103/MT202/pacs.009 ADV) that has been settled through cover (pacs.009 COV, MT202 COV, pacs.009 (in case of ADV)). In such cases, the system parks the cancellation request in the manual queue for user actions.

The possible scenarios of receiving cancellation request for the payment settled through cover are as follow:

- Customer or Creditor is already credited when the cancellation request is received



- Customer or Creditor is not yet credited. Cover is rejected or returned by the reimbursement agents.

![Machine generated alternative text:
s.008 announcement
Bank A
Bank B
acs.oos COV
pacs.004/pacs.002
(Return/Reject Cover)
Bank C
acs.oos COV
pacs.004/pacs.002
(Return/Reject Cover)
waiting settlÅm
Bank D
Cover will never be received
for ann ncement
pt Recall - camt.02
Recall - camt.029 with reason cod
Response - camt.029 with reason cod
Bank B
Parked awaiting cover
Payment Status : 130
Park for manual
action
Operator
Accepting to cancel the
Payment Status : 998
announcement message
Payment Status : 130
Payment Status : 130 ](../../Resources/Images/4205737/User Guide 1 International_9.png)

- Customer or Creditor is not yet credited. Cover is not rejected or returned by the reimbursement agents.



The following are the possible user actions:

| Action | Description |
| --- | --- |
| Accept | When the user accepts the cancellation request, the system displays an override for the user to create the return manually for the cover message and sends to the correspondent bank since the fund is transferred through the cover message. Once the user accepts this override, the system generates the camt.029 and sends to the assigner of the cancellation request with status code as CNCL and updates the cancellation request status as Accepted. Audit trail of the transaction is updated as ‘Inward Cancellation request is accepted’. |
| Reject | When the user rejects the cancellation request, the system generates the camt.029 message with RJCR status code and updates the cancellation request status as Rejected. The system marks the Recall status in the announcement and cover message (if present) as Rejected, so that the payment can be released or submitted from repair queue for processing (if present in the repair status). Audit trail of the transaction is updated as ‘Inward cancellation request is rejected’. |
| Pending | When the user sends the pending response for the cancellation request, the system generates the camt.029 message with PDCR status code and the cancellation request remains in the queue for manual action. Audit trail of the transaction is updated as ‘Pending response is sent for the cancellation request’ |

[Accepting Cancellation Request – Customer or Creditor is Credited](#)

If the customer or creditor is already credited, the user must debit the customer by creating a new transaction (book payment) from the standard order entry book transfer screen or reversing the original transaction using the Reversal Payment screen.

- Accounting entry for the new OE Book payment is
  - Dr Customer
  - Cr Hold for cover suspense account

Once the customer is debited, the user has to create a return message for the cover and send it out to the correspondent bank.

[Cover Message Received from Reimbursement Agent](#)

If the cover message is received from the correspondent bank as pacs.009 COV message, the user has to manually generate the cover return from the **Return of SWIFT Completed Credit Txn** enquiry in the below menu.

**User Menu** > **Payments** > **Payment Hub** > **Payment Investigations and Cancellations** > **Return/Reject Payment** > **Return of SWIFT Completed Credit Txn**.

While accepting a cancellation request and while initiating a manual return, the originator details should be the same. For example, if the user selects the *Response Originated By* field as “Customer” while accepting the cancellation request, then user should select “Customer” in the *Return Originated By* field while returning the payment manually.

Once the cover message is returned, the system updates the status of the cover message as ‘Completed with Return’ and direct announcement message as ’Completed with Return’, if it is already in status ’Completed’.

- If the user has created a book transfer to debit the customer, then the system marks the status of the direct announcement message (MT103, pacs.008) as ‘Completed with Return’, once the return is generated from the enquiry.

- If the user has reversed the original transaction from reversal screen to debit the customer, then the system would have been updated the status of the direct announcement message to ‘Reversed’ already.

[Credit Notification Received from Reimbursement Agent](#)

If the credit notification (camt.053 or MT910) is received from the correspondent bank instead of cover message, the user has to manually create a return message (pacs.004) from the **Outgoing ISO Bank Transfer Return** OE screen in the **User Menu** > **Payments** > **Payment Hub** > **Initiate Payment Transaction** > **Initiate ISO Bank Transfer** > **Outgoing ISO Bank Transfer Return** menu. While initiating the return, the user has to enter the FT number of the direct announcement message in the Return screen, so that once the return is generated, the system updates the announcement message as Completed with Return.

The accounting entries below are raised for the Return payment.

- Dr Cover suspense account
- Cr Nostro account

[Cover Received after Receiving Cancellation Request for Announcement Message](#)

If the cover message is received after receiving the cancellation request for the announcement message, then the system parks the cover message in the repair queue for user action. If the cancellation request is received for the announcement message and it is not in the Rejected status, then the system marks the received cover message for the cancellation request and parks in the repair queue.

[Accepting Cancellation Request – Customer or Creditor is not Credited - Cover Message is not Received](#)

If the Temenos Payments Hub bank does not receive the cover message (cover may get rejected or returned by reimbursement agents), then the system marks the announcement message as Rejected and updates the Recall status of the payment as Accepted. There is no need to send pacs.002 RJCT for the announcement message. The system also updates the Recall status in the cover message as Accepted once it is received and parked in the repair queue. The user can reject or return the transaction from the repair queue based on the settlement method.

[Automatic Pending Response for Cancellation Request](#)

A bank can configure to send pending response to the assigner of the CBPR+ cancellation request if the user has not performed any action on the request on the date of receipt of the cancellation request. If the pending response is already sent manually on the date of receipt of cancellation request, the system does not send this automatic response. The system triggers this automatic response during the EOD process, if the bank has configured to send the pending response. This automatic response is triggered only once for each cancellation request.

| Direction | Processed Successfully | Status code | Reason code | Additional Information |
| --- | --- | --- | --- | --- |
| Incoming | YES | PDCR | RQDA | NA |
| Incoming | NO | PDCR | NOAS | Cancellation request is being investigated |

[Unmatched Cancellation Request](#)

On receiving the incoming cancellation request, Temenos Payments Hub bank checks for the configuration in the Clearing Setting table to verify whether to send out an automatic negative response for the cancellation request or not.

- If the configuration is set to be automatic, then Temenos Payments Hub generates camt.029 message with RJCR status code and NOOR reason code and send to the assigner of the cancellation request.
- If the configuration is set to be manual, the system parks the cancellation request message for the manual action with status as Unmatched, and it is available for the user to take action in the **Inward Cancellation Req- Require Manual action** enquiry from the **User Menu** > **Payments** > **Payments Hub** > **Payment Investigation and Cancellations** > **Cancellations** > **SWIFT ISO Cancellations** > **Inward Cancellation Req- Require Manual action** menu.

The following are the possible user actions:

| Action | Description |
| --- | --- |
| Accept | When the user accepts the unmatched cancellation request, the user must enter the valid transaction reference number to match it with the cancellation request.   - If the user does not enter any value for matching, the system displays an error message for the user to enter the value. - If the user enters a value and if it is not present in the system (Transaction got processed in legacy system and cancellation request received in the new system), then the system displays a warning message for the user to indicate that the original payment is not found to accept the cancellation request. If the user accepts the warning message, the system generates a Resolution of Investigation (camt.029) message with CNCL status code and sends out to the assigner of the cancellation request. If the user does not accept the warning message, the system does not accept the cancellation record. - If the user has entered the FT number of the transaction which is already returned, rejected, cancelled,reversed, or seized, then an error message gets displayed on the screen as “Acceptance not allowed”. User has to change the FTnumber with a valid status or user can only reject the cancellation request - If the user accepts the cancellation request for the payment that is not present in the system, the user has to manually initiate a return and send to the instructing agent of the transaction.  - If the original transaction is a customer transfer, the user has to create a return from ISO CTR return OE screen from the **User Menu** > **Payments** > **Payment Hub** > **Initiate Payment Transaction** > **Initiate ISO Customer Transfer** > **Outgoing ISO Customer Transfer Return** enquiry. - If the original transaction is a bank transfer, the user has to create a return from the ISO BTR return OE screen from the **User Menu** > **Payments** > **Payment Hub** > **Initiate Payment Transaction** > **Initiate ISO Bank Transfer** > **Outgoing ISO Bank Transfer Return** enquiry. |
| Reject | When the user rejects the cancellation request, the system generates the camt.029 message and sends to the assigner of the cancellation request with RJCR status code and the user selected reject reason code. Eventually, the cancellation request status gets updated as Rejected. |
| Pending | When the user sends the pending response for the cancellation request, the system generates the camt.029 message with PDCR status code and the user selected pending reason code. The cancellation request remains in the queue for manual action. |

Before sending camt.029 response for any action, RMA needs to be checked. Only if RMA is present, the system generates and sends the message. Otherwise, the system displays an error message and the cancellation message remains in the manual queue. The user has to create RMA manually to send the camt.029 message.

After validating and submitting the user action on the record, the system parks the record in the authorisation enquiry (given below).

**User Menu** > **Payments** > **Payments Hub** > **Payment Investigation and Cancellations** > **Cancellations** > **SWIFT ISO Cancellations** > **Authorise Inward Cancellation Requests**.

[Process Transmission Reports and Delivery Notification for Outgoing Resolution of Investigation Message](#)

When sending out the Resolution of Investigation (camt.029) message to the SWIFT network, it is possible to receive negative acknowledgement or negative DLN from the network. In such cases, the messages are parked in the SWIFT ISO Technical exception queue.

When the user clicks the Accept option for the message from an exception enquiry, the status of the cancellation record gets updated as ‘NetworkRejected’. The Cancellation record is available for the user action in the manual queue.

If the user has already accepted the cancellation message, the return or reject message got generated previously, and if the same accept action is triggered again for the cancellation message, then the system does not generate the return or reject message. The system generates only the Resolution of Investigation message (camt.029) and sends again to the SWIFT network.

Refer to the [Processing of Non – Payment messages based on Technical Acknowledgement](../../../PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm#ProcessNonPayment) section for more information on further possible actions for camt.029 message from technical exception enquiry.

[Generating Alert When Cancellation Request Requires Manual Action](#)

Temenos Payments Hub bank triggers an alert to a client bank’s system when an incoming cancellation request (camt.056) is received and parked in a queue for manual action. This notification is published by Temenos Payments Hub to notify that inward camt.056 is received and needs action. To view this alert,

1. Go to **User Menu** > **Payment Hub** > **Payment Inquiries** > **Pending and Processed Payments** > **Payments Enquiry – Transaction wise**.
2. Enter the filter criteria to filter the transactions.
3. From the **Pending and Processed Payments** page, click .
4. In the **Payment Information** window, select the Alerts and Notification option from the drop-down to view the alerts generated for the transaction.

This alert feature is available in Temenos Payments Hub only from R22 release.

[API for Cancel Request Processing](#)

Temenos Payments Hub bank exposes an API for the client bank’s system for the client to respond to a recall request. The client can respond with positive or negative responses for the cancel request using an API. Once the responses reach Temenos Payments Hub, the process continues as per the normal flow for cancellation request for cross border international payments.

Bank also exposes another API to the client bank’s system for the client to view the reject and pending reason codes while responding to a cancellation request.

Refer to the [API catalogue](https://apidocs.temenos.com/open-banking) for more information.

[](#)[Initiating Outward Cancellation Request](#)

Banks can initiate outward cancellation request for outgoing SWIFT CBPR+ payments using the below mentioned enquiries. To access all the menus and enquiries related to SWIFT ISO Outward and Inward Cancellation processing, the bank requires PPSWCR license in addition to PPSWMX license. The system allows to use the SWIFT ISO recall initiation enquiries only when the processing Temenos Payments Hub bank is SWIFTMX enabled.

The SWIFT User Handbook does not have separate scenarios like client initiated or bank initiated recall, whereas similar scenarios are there for SEPA. Temenos Payments Hub provides separate enquiries for client initiated and bank initiated recalls.

[Initiating Customer Initiated Cancellation Request](#)

The bank operators use the customer initiated enquiry to initiate a cancellation request for cross-border SWIFT payments based on the request from the debtor (on behalf of ordering customer). The request may come from debtor in verbal, written, or electronic format.

Using this enquiry, the bank users can initiate cancellation request for a serial or announcement message sent through SWIFT network. If a cross-border SWIFT payment is settled using cover method, this enquiry does not allow recalling the cover. Cover cancellation request can be initiated only through the bank initiated enquiry. Refer to the [Initiating Bank Initiated Cancellation Request](#IniBankIni) section for more details.

Below is the navigation for the enquiry to create customer initiated cancellation request.

**User Menu** > **Payments** > **Payments Hub** > **Payment Investigation and Cancellations** > **Cancellations** > **SWIFT ISO Cancellation** > **Create Cancellation Requests** > **Customer initiated Cancellation Request**.

The user can enter either FTNumber, UETR, or both as search criteria to select the required payment record, which can be in live or archive. In order to fetch an older payment, which is already archived, the user must search using FTNumber. Based on the search criteria, the system fetches the payment and display on the enquiry output screen. The user can initiate cancellation request for a payment if the following conditions are met:

- Outgoing payment is in system (in live or archive)
- Outgoing CBPR+ or SWIFT FIN payments (customer or bank) that are successfully processed. In case the payment is sent through cover, the underlying message is sent as CBPR+ or SWIFT FIN
- Selected payment must be one of the recall allowed message types that are configured at the clearing configuration. Refer to the [Message Types for Recall](../../../PPSWMX/International_PaymentsCBPR/PPSWMX/Configuration.htm#202207a) section for more details.

For SWIFTMX, the following message types are configured for recall:

- Customer transfer - pacs.008, MT103
- Bank transfer - pacs.009, MT202
- Cover Payment – COV
- Bank Transfer Advice – pacs.009AD

- In case of cover, Return or Reject for the cover is received and processed. Therefore, the underlying payment might have been moved to returned or rejected status. Such payments are also displayed, so that the user can initiate recall for the direct or announcement message
- Cancellation request for the payment

- has not been sent already.
- sent earlier but received negative technical acknowledgement, or
- sent earlier and did not receive response for the configured overdue days

- As per SR2026 standards, request for cancellations for underlying SWIFT CBPR+ Customer Credit Transfers are routed to Tracker BIC. This is applicable only for customer transfer.
- CBPR+ Channel-specific validations are successful to check whether the available data conforms to the cancellation message format.
- Acceptance days not set as N in the records of the Clearing Setting table and the sum of the credit value date and the configured acceptance days is less than or equal to the date when the recall is initiated. Refer to the [Message Types for Recall](Configuration.htm#202207a) section for more details.

In case the system sends the payment through cover and the cancellation request is already sent for the cover and awaiting response, the system still allows to initiate cancel request for the underlying payment with an override information to the user.

If all these conditions are met, the user can submit the cancellation request by providing:

- Mandatory cancel reason code (ISO or Proprietary reason applicable for CBPR+).

CBPR+ allows only ISO reason code (Proprietary reason code is not allowed).

The allowed reason codes are displayed in a dropdown and is configured in system

- Optional additional information as textual data. The system allows maximum two lines of additional information to be captured with each line supporting maximum 105 characters.

Since the cancellation is requested by the ordering customer, the originator fields are populated with the debtor details (ordering customer) from the underlying payment. The creator fields are not populated for customer initiated cancellation. After the supervisor authorizes the cancellation request, the system generates the final message as per the CBPR+ format.

[](#)[Initiating Bank Initiated Cancellation Request](#)

The bank operators use the Bank Initiated Cancellation Request enquiry to initiate a cancellation request for cross-border SWIFT payments based on the requirement of the bank (cancellation is not requested by ordering customer).

Below is the navigation for the enquiry to create bank initiated cancellation request.

**User Menu** > **Payments** > **Payments Hub** > **Payment Investigation and Cancellations** > **Cancellations** > **SWIFT ISO Cancellation** > **Create Cancellation Requests** > **Bank Initiated Cancellation Request**.

The user can enter either FTNumber, UETR, or both as search criteria to select the required payment record, which can be in live or archive. In order to fetch an older payment, which is already archived, the user must search using FTNumber. Based on the search criteria, the system fetches the payment and display on the enquiry output screen. The user can initiate cancellation request for a payment if the following conditions are met:

- Outgoing Payment is available in the system (in live or archive)
- Outgoing payment can be a serial or a cover payment sent through SWIFT

In case a cross-border payment is sent using the cover method, the announcement is always sent through SWIFT (as CBPR+ pacs.008). Hence, the recall for the announcement can be sent only from SWIFT ISO Cancellation enquiry. However, the cover can be sent either through SWIFT (as CBPR+ pacs.009 COV) or through a RTGS clearing (for example, as pacs.009 COV through TARGET2). The user can use either this CBPR+ enquiry or RTGS enquiry (Bank Initiated Cancellation Request under RTGS Cancellation menu) to create cancellation request for the cover sent through RTGS clearing.

- Selected payment must be one of the recall allowed message types that are configured at the clearing configuration. Refer to the [Message Types for Recall](Configuration.htm#202207a) section for more details.

For SWIFTMX, the following message types are configured for recall:

- Customer transfer - pacs.008, MT103
- Bank transfer - pacs.009, MT202
- Cover Payment - COV
- Bank Transfer Advice - pacs.009AD

- For payment that is settled through cover, the system would have received and processed the Return or Reject for the cover. In such cases, the underlying payment might have been moved to the returned or rejected status. Such payments are also displayed, so that the user can initiate recall for the direct or announcement message

Likewise, if Reject is received for a direct or underlying payment sent through cover method, the system routes it to SWIFT ISO Business exception enquiry and the user has the option to choose reverse or return from this enquiry. On choosing the reverse option, the underlying payment is moved to the ‘Rejected’ status. The user can still initiate recall for the cover in this scenario.

- Cancellation request for the payment

- has not been sent already,
- sent earlier but received negative technical acknowledgement, or
- sent earlier and did not receive response for the configured overdue days

- As per SR2026 standards, request for cancellations for underlying SWIFT CBPR+ Customer Credit Transfers are routed to Tracker BIC. This is applicable only for customer transfer.
- CBPR+ Channel-specific validations are successful to check whether the available data conforms to the cancellation message format
- Acceptance days not set as N in the records of the Clearing Setting table and the sum of the credit value date and the configured acceptance days is less than or equal to the date when recall is initiated

In case the payment is sent through cover and cancellation request is already sent for the cover and awaiting response, the system still allows to initiate cancel request for the underlying payment with an override information to the user.

If all these conditions are met, the user can submit the cancellation request by providing:

- Mandatory cancel reason code (ISO or Proprietary reason applicable for CBPR+).

CBPR+ allows only ISO reason code (Proprietary reason code is not allowed).

The allowed reason codes are displayed in a dropdown and is configured in the system.

- Optional additional information as textual data. The system allows maximum two lines of additional information to be captured with each line supporting maximum 105 characters

Since the cancellation is initiated because of bank decision (not based on customer request), creator BIC is populated as processing bank BIC and the originator fields are not populated. After the supervisor authorizes the cancellation request (Refer to the Authorise Outward Cancellation Request section), the system generates the final message as per the CBPR+ format.

[Other Related Enquiries for Outward Cancellation Request](#)

In case the payment is sent through cover method where the cover is sent through ISO based RTGS clearing (underlying sent through SWIFTMX) and the cancellation request is initiated for the cover, then such cancellation records are listed in both RTGS and SWIFT ISO enquiries.

Below are the enquiries for authorizing and viewing outward cancellation request.

- **Authorise Outward Cancellation Request**: This enquiry displays all the CBPR+ Bank and Customer Initiated recall and cancellation requests submitted by the users and pending for authorization. Bank supervisors can use this enquiry to authorize the pending requests.

**User Menu** > **Payments** > **Payments Hub** > **Payment Investigation and Cancellations** > **Cancellations** > **SWIFT ISO Cancellation** > **Create Cancellation Requests** > **Approve outward Cancellation Request**.

- **Delete Unapproved Outward Cancellation Request**: This enquiry displays the outgoing cancellation requests that are pending for authorization and allows the users to delete such unapproved cancellation requests

**User Menu** > **Payments** > **Payments Hub** > **Payment Investigation and Cancellations** > **Cancellations** > **SWIFT ISO Cancellation** > **Create Cancellation Requests** > **Delete Unapproved outward Cancellation Request**.

- **Outward Cancellation Request-Pending Response**: This enquiry displays specific outgoing recall and cancellation requests sent and waiting for response (neither cancel nor reject response received)

**User Menu** > **Payments** > **Payment Hub** > **Payment Investigations and Cancellations** > **Cancellations** > **SWIFT ISO Cancellations** > **Outward Cancellation Request-Pending Response**.

The list has options that enables the user to view the related transaction, details of the recall request, and generated recall messages.

- **Outward Cancellation Req – Network/Clearing Rejected**: This enquiry displays specific outgoing recall and cancellation requests sent, and received negative acknowledgement from network, interface or negative delivery notification or negative ack from Clearing

**User Menu** > **Payments** > **Payment Hub** > **Payment Investigations and Cancellations** > **Cancellations** > **SWIFT ISO Cancellations** > **Outward Cancellation Req – Network/Clearing Rejected**.

The list has options that enable the user to view the related transaction, details of the recall request, and generated recall message.

- **Outward Cancellation Request - View Status**: This enquiry displays all the outgoing recall and cancellation requests sent and their current status.

**User Menu** > **Payments** > **Payment Hub** > **Payment Investigations and Cancellations** > **Cancellations** > **SWIFT ISO Cancellations** > **Outward Cancellation Request - View Status**.

The list has options that enable the user to view the related transaction, details of the recall request, generated recall message and recall response.

[Receiving Resolution of Investigation (camt.029)](#)

- After a cancellation request is sent to the correspondent bank, the system can receive Positive (CNCL), Negative (RJCR), or Pending response (PDCR) in camt.029 format based on the action taken by the assignee of the cancellation request.
- Incoming camt.029 responses from SWIFT and first received in the Delivery module, which in turn forwards the full message (containing Technical and Business application headers) to Temenos Payments Hub. Temenos Payments Hub extracts the camt.029 document, stores the full message and validates against the XSD. As the system receives multiple camt.029 responses against an outward camt.056, the system stores them separately.
- The system identifies the CBPR+ original cancel request for incoming camt.029 using Resolved Case Identification in the incoming camt.029 message matched with case identification in the related cancel request (sent as case ID in camt.056). For an outgoing cancellation request, Temenos Payments Hub generates the case ID. The system also checks whether the Assigner BIC of camt.029 is same as the Assignee BIC of outward camt.056

- If a matching record is not found, then the system marks the incoming camt.029 as unmatched.
- If the matching record is found and is awaiting response (CANCELLATIONSENT status), the system stores the camt.029 response details such as Assignment Identification, Cancellation Status Identification, reject or pending reason code along with additional information against the cancel request.

The system updates the cancel request status as per the response received (CANCELACCEPTED or CANCELREJCTED).

For pending response, the status remains unchanged as CANCELLATIONSENT.

The system also updates the audit trail and recall status (for serial) in the related transaction.

For acceptance status, the system updates only the cancel request status. Reversal of the accounting entries of underlying payment and updating the transaction status to returned (996) or reversed (998) happens only on receipt of pacs.004 and pacs.002. The system also updates the transaction reference of pacs.004 and pacs.002 in the related cancel request.

- The system has the ability to mark the cancel request as OVERDUE if the camt.029 response is not received within the configured overdue days at the clearing setting level. If the system receives the response after the cancel request is marked OVERDUE, the system still stores the camt.029 details. In case of positive status, the system updates the status of the cancel request to CANCELACCEPTED. For negative and pending status, the status remains unchanged as OVERDUE.

[Viewing Outward Cancellation Requests from Pending Processed Payments Enquiry](#)

When the Temenos Payments Hub bank sends a cancellation request, the system has the ability to display the cancellation request details and its responses (Resolution of Investigation message - camt.029) from the underlying payment.

To view the cancellation request details,

1. Go to **User Menu** > **Payments** > **Payment Hub** > **Payment Enquiries** > **Pending and Processed Payments**.
2. From the list, click ’View In Details’ option across the necessary request.
3. Select the ‘View Outward Cancellation Requests enquiry’ option from the drop-down and click /4205685.png) .

The user can also view the acknowledgement received for the outward cancellation request using the above enquiry.

[API for Initiating Outward Cancel Request](#)

Temenos Payments Hub bank exposes APIs for the client bank’s system, so the user can create bank initiated or customer initiated recall requests (CBPR+ or RTGS).

API is allowed to create cancel request only for serial and direct payments and not for cover payments.

Refer to [API Catalogue](https://developer.temenos.com/) for details about API catalogue.

In case Temenos Payment Processing bank is not SWIFT MX enabled and recall is initiated for the payments (serial message and direct or underlying message if settled through cover method) sent through SWIFT channel, then the API returns an error.

## Processing Customer Payment Cancellation Request

The initiating party or the forwarding agent issues the customer payment cancellation request message to request the cancellation of an initiation payment message that is previously sent. There is no MT equivalent for this message currently.



The user requires the PPSWCR license to accept and process the customer payment cancellation request in ISO format from SWIFT.

A customer payment cancellation request message (camt.055) from SWIFT concerns only one original payment instruction at a time. When a case assignee performs a cancellation successfully, it must return the corresponding funds to the case assigner.

Temenos Payments Hub supports the customer cancellation request through camt.055 or API. Temenos Payments Hub supports camt.055 from SWIFT only for the payment instruction received through pain.001 and is not a part of a batch. Similarly, Temenos Payments Hub supports the customer cancellation request through API only for the transactions that are not the part of batch processing.

Customer cancellation requests can be processed as STP or non-STP based on the source parameter configuration.

- If configured as STP, the system processes the customer cancellation request based on the underlying transaction status without waiting for manual intervention.
- If configured as non-STP, the system parks the received customer cancellation request in the manual enquiry under “Customer Cancellation Req - Require Manual Action” for user action. From the enquiry:
  - When the user selects the ‘Accept’ action, the system processes the camt.055 based on the underlying transaction status, similar to STP processing.
  - When the user selects the ‘Pending’ action, the system generates and sends the pending response camt.029 to the customer.
  - When the user selects the ‘Reject’ action, the system generates and sends the reject response camt.029 to the customer.

[Initiating Customer Cancellation Request through API](#)

Temenos Payments Hub exposes API for the client bank system to initiate a customer cancellation request for a payment instruction that is not a part of the batch processing. Once the system receives the API request for cancellation, the process is similar to the camt.055 received through SWIFT network.

The source for the cancellation request received through API is decided based on the source of the underlying transaction. While inputting the cancellation request through API, if the user inputs both Party and Agent tags for the Case creator, then the latest tag that is present for the creator gets updated as a part of the cancellation record.

Refer to the [Temenos Developer Portal](https://developer.temenos.com/) to know more details about the API catalogue.

[Pre-Validations for cancellation request received as camt.055](#)

Pre-validation for the cancellation request received as camt.055 includes the following processes.

[Processing CBPR camt.055 after the SWIFT MX Release year](#)

Temenos Payments Hub can process camt.055 CBPR+ message only if the release year in which the customer cancellation request message camt.055 goes live (2023) is either the current release year or the previous release year of the current SWIFT MX release installed in the bank.

If the SWIFT MX release year for the customer cancellation request is not the current camt.023 release or the current release is less than the customer cancellation request release (2023), then the system does not process the camt.055 and marks the status of the camt.055 file as ‘REJECTED’ along with error text ‘Processing Company does not have the SWIFT MX release for camt.055 message’. The system does not create any case record.

[Validating NETTING.AGREEMENT for Customer Payment Cancellation Request](#)

The sender of the cancellation request must have the authority to send the cancellation request which is validated by the presence of a NETTING.AGREEMENT record with the sender. The cancellation request is rejected in the absence of a NETTING.AGREEMENT and the customer is informed based on the acknowledgment agreement defined in the NETTING.AGREEMENT or in the MESSAGE.ACCEPTANCE parameter.

If the bank does not wish to perform the netting agreement check for the camt.055 message, this can be achieved through configuration (NO.DA.LIST table).

If the configuration is available for the message type in NO.DA.LIST, then the system checks the default NETTING.AGREEMENT record and processes the message based on the default record. If there is no record found is NO.DA.LIST, then the system validates the message based on the specific record for the sender. If the specific record is not found, then the system updates the status of the file as REJECTED.

[Performing Technical Duplicate check](#)

Temenos Payments Hub performs a technical duplicate check on the received file based on the ‘Business Message Identifier’ tag in the message. If the file is identified as duplicate, then the system marks the status of the received file as REJECTED.

[Locating Original file](#)

The system locates the original payment Initiation file (pain.001) for which the cancellation request is received based on the Original Message Identification and Original Message Name Identification tags present in the message. If the file is not available, then the system rejects the customer payment cancellation request.

[Performing Duplicate Check](#)

Temenos Payments Hub performs the duplicate check to determine if there are any existing cancellation request received for the same payment. The system performs this check using Unique End to end Reference (UETR) and Original message identification against the incoming cancellation requests received. The user can configure the criteria for the duplicate check for the customer cancellation request at the message mapping parameter table when the default criteria is not applicable.

- If the previous request is rejected, then the system accepts and processes the new cancellation request.
- If the action is still pending for the previous request, then the case management system ignores the new request.
- If the previous request was accepted successfully, then system rejects the new cancellation request and updates the status as CANCELREJECTED. If the system has to send an acknowledgment, it sends a negative resolution of investigation message camt.029 with RJCR status code and ARDT reason code.

A duplicate check is done for the customer cancellation request received through API as well.

[Locating Original Transaction](#)

The system locates the original transaction for which the cancellation request is received using Unique End to end Reference (UETR), Original End to End identification, and Original Instruction Identification. The system customises the above criteria, which is specific for camt.055 from SWIFT through an API in the message mapping parameter table, as the criteria is different from the default criteria in the system. Live and archive database is searched for the underlying transaction.

If the system is unable to locate the original transaction, it updates the customer cancellation request (camt.055) as CANCELREJECTED and the process indicator of the record as UNMATCHED.

For the matched transaction, the system does not require the SWIFT to check the number of allowed days within which the cancellation request must be received for the payment. Hence, the corresponding configuration for allowed days of cancellation request in the CLEARING.SETTING table is left blank.

[Sending Resolution of Investigation Message to Initiating Party or Forwarding Agent](#)

When the system decides to accept or cancel the customer cancellation request received through camt.055) based on the system status, the decision to send an ROI message (camt.029) depends on the acknowledgment configuration defined in netting agreement or message acceptance or source setting level.

Bilateral agreement for ROI message can be defined at the following levels in the system:

- NETTING.AGREEMENT: Checked for File and transaction level ROI. The user can define the agreement for a particular sending agent. Separate indicators exists for file and transaction level acknowledgments.
- MESSAGE.ACCEPTANCE: Checked for file level ROI. The user can define the agreement for cancellation requests received from all agents through SWIFT.
- SOURCE.SETTING: Checked for transaction level ROI. The user can define the agreement for cancellation requests received from all agents through SWIFT.

Priority is given to the netting agreement. If the acknowledgment report indicator is not defined in the netting agreement, then the system looks up the indicators defined in Message acceptance (file acknowledgment) or Source Setting (transaction acknowledgment) to determine if an ROI message must be generated.

File level ROI is considered in the below scenarios when the system rejects the cancellation request.

- Technical Duplicate
- Underlying pain.001 is not located

Transaction level ROI is considered in the below scenarios when the cancellation request is rejected or accepted.

- Case Duplicate
- Underlying transaction is not located
- Based on the status of the payment or the response received for an outgoing cancellation request

This acknowledgement is not applicable to the customer cancellation request received through API.

Refer to the [Configuration](Configuration.htm) section for more details.

[Processing Cancellation Based on Transaction Status](#)

Cancellation processing depends on the business state of the underlying transaction. If the transaction status matches the allowed cancellable statuses for customer initiations received from SWIFT, then the system continues to process the request based on the payment status. Else the system marks the request as CANCELREJECTED if the source parameter configuration is 'Blank'. If the configuration is enabled to process it as Non-STP, the system displays the error message, “Cancellation request cannot be accepted due to invalid transaction status”, when the user accepts the cancellation request from the manual enquiry.

If the underlying payment has reached the final status (success or failure), then the system does not consider the above configuration.

[](#)[Receiving Customer Cancellation Request for a payment already Cancelled, Returned, Reversed, Rejected and Seized](#)

On receiving customer cancellation request for a payment that is already in Rejected (998), Returned (996), Reversed (993), Cancelled (997), Seized (995) status, the system rejects the request and marks the status of the customer cancellation record as CANCELREJECTED. For the Returned status, the reason code in the negative response is Already Returned (ARDT) and for the Seized status, the reason code in the negative response is LEGL. For the other statuses, while sending the negative response for the cancellation request, the system checks for the applicable reason code in the clearing return code table and the same is mapped in the response.

[Receiving Customer Cancellation Request for On Us Payment](#)

On receiving the customer cancellation request for a transaction where the beneficiary holds an account in Temenos Payments Hub, processing depends upon the payment status.

- If the transaction is processed successfully (status 999), then the system rejects the request and marks the case status as CANCELREJECTED with reason code AGNT (Agent Decision) for STP and non-STP ‘Accept’ action.
- If the beneficiary is not yet credited, then the system accepts the request and marks the case status as CANCELACCEPTED. Also, the system cancels the transaction and marks the status as CANCELLED with the cancel reason code FOCR (Following Cancellation Request) for STP and non-STP ‘Accept’ action.

[Receiving Customer Cancellation Request for Payment Awaiting Response for Fund Reservation Request / Posting Request](#)

On receiving the customer cancellation request for a payment that is awaiting response for a fund reservation request (Status code - 641) or waiting for the posting response (Status code – 662) which could be the case in standalone mode, the system rejects the request and the marks the case status as CANCELREJECTED with the reason code AGNT (Agent Decision). For both STP and non-STP, the behaviour is the same. From the manual enquiry, the user can only reject this cancellation request. When the user tries to ‘Accept’ the request, the system displays an error message “Cancellation request cannot be accepted due to invalid transaction status”.

[Receiving Customer Cancellation Request for Payment Not Sent to Clearing/SWIFT](#)

On receiving the customer cancellation request (camt.055) for a transaction that is not yet sent to clearing/SWIFT, the system accepts the request and marks the case status as CANCELACCEPTED. If the customer is already debited, then the system reverses the accounting entries of the transaction so the customer is credited back. Also, the system marks the transaction as CANCELLED with cancel reason FOCR (Following Cancellation Request).

This behaviour is the same for both STP and non-STP processing.

[Receiving Customer Cancellation request for Payment that Received Negative Acknowledgement or Negative DLN from Clearing/SWIFT](#)

On receiving the customer cancellation request (camt.055) for a payment that has received a negative ACK from clearing/network or a negative DLN from the network (Status code - 680), the system accepts the request and marks the case status as CANCELACCEPTED.

The system marks the underlying transaction as CANCELLED (status - 997) with cancel reason FOCR (Following Cancellation Request). The system reverses the accounting entries of the transaction (no new reversal transaction is created) and sends the customer status report (pain.002) to the customer based on the configurations defined in netting agreement or source setting.

This behaviour is the same for both STP and non-STP (Accept) processing.

[Decision to Send Cancellation Request to Clearing/SWIFT based on Customer Cancellation Request](#)

If the underlying transaction is already sent outside to the clearing or the correspondent bank, the system forwards the cancellation request to the clearing or the correspondent bank based on the configuration of the source from which the customer cancellation request is received.

If forwarding is not enabled, then the system rejects the customer cancellation request, and marks the case status as CANCELREJECTED with the reason code NARR and the reason description ‘Cancellation request cannot be forwarded'.

If forwarding is enabled, the cancellation request is only forwarded if the clearing/SWIFT validations for the cancellation request are successful. SWIFT/Clearing specific validations are as follows:

- The system initiates the cancellation request to the clearing within the allowed business or calendar days as per the clearing scheme rules (if configured). If it is beyond the allowed days, the system marks the customer cancellation record as CANCELREJECTED with the reason code NARR and the reason description ‘Cancellation request cannot be forwarded to a net agent as it exceeds the maximum number of allowed days allowed by the clearing’.
- Clearing/SWIFT should accept the recall messages for the underlying transaction. If the clearing does not have the recall capability, then the system marks the cancellation record as CANCELREJECTED with the reason code NARR and the reason description ‘Recall not supported by the Clearing for the Credit Transfer’.
- For the cancellation request sent to the correspondent bank through SWIFT, the processing bank must be MX enabled to send out FI to FI cancellation request message through SWIFT. If the bank is not MX enabled, the system updates the cancellation record as CANCELREJECTED with reason code NARR and the reason description as ’Cancellation request cannot be forwarded to the next agent as the Temenos Payments Hub processing company is not MX enabled’.
- For the cancellation request sent to the correspondent bank through SWIFT, SWIFT requires the existence of RMA with the assignee bank for the cancellation request. If RMA is not present or defined, the system marks the cancellation record as CANCELREJECTED with the reason code NARR and the reason description as ’RMA doesn’t exist for sending cancellation request camt.056 to the next agent’.

On successful validation of clearing specific checks, the system generates the FI to FI cancellation request (camt.056) and sends it out to the Instructed Agent of the underlying transaction.

On a failure of clearing validations to send the FI to FI cancellation request, the system marks the cancellation record status as CANCELREJECTED with the reason code NARR.

This behaviour is the same for both STP and non-STP processing. For non-STP, when the user tries to ‘Accept’ the requests for the above-mentioned scenarios, the system displays the error message on the screen.

[Receiving Customer Cancellation Request for Payment Settled Serially](#)

The system sends a cancellation request to clearing or SWIFT based on the customer cancelation request in the following scenarios:

- Underlying payment is completed successfully, and accounting entries are raised (Status code - 999)
- Underlying payment is sent successfully to clearing or network and is waiting for an acknowledgement (Status code - 677)
- Underlying payment is sent successfully to the network and has received network acknowledgement but is waiting for DLN (Status code - 673)
- Underlying payment is in completed status but has received business reject (pacs.002 RJCT) from the creditor bank. Payment is waiting in the business exception queue for the user to take action. (Status code - 999)

A new FI to FI cancellation request case record is created in the system. After the system sends the request to the instructed agent of the underlying transaction (through clearing or SWIFT), the system marks the status of this record as CANCELLATIONSENT and the status of the customer cancellation record as CANCELLATIONSENT.

The customer cancellation record and the FI to FI record are linked through the case ID present or created for the customer cancellation request.

This behaviour is the same for both STP and non-STP (Accept) processing.

[Receiving Customer Cancellation Request for Payment Settled Through Cover](#)

This section explains the process of receiving a customer cancellation request for the payment settled through cover.

[Sending FI to FI Cancellation Request to Receiver of Announcement message](#)

On receiving the customer cancellation request (camt.055) for the transaction settled through the cover method, the system creates the FI to FI cancellation request (camt.056) and sends it to the receiver of the announcement message in the following scenarios:

- An announcement message is sent out and has received a positive acknowledgement, and is waiting for the Delivery Notification (DLN). In this case, a cover is released and sent to the correspondent bank through clearing or network as acknowledgment was received for the announcement message.
- An announcement message is sent out and has received positive acknowledgement and Delivery Notification (DLN). A cover message is released to the correspondent bank through clearing or network and cover message is waiting for acknowledgment or Delivery notification.
- An announcement message and a cover message are sent out. The instructed agent of the announcement message rejects the message by sending a pacs.002 RJCT message. The message is parked in a business exception enquiry for manual action.
- An announcement message and a cover message are sent out, and the payment is marked as complete (status 999). The bank initiates the FI to FI Cancellation request for the cover message from the ‘Bank Initiated Cancellation Request’ enquiry present under the SWIFT ISO cancellation request menu. The system generates a cancellation request camt.056 and sends it out to the receiver of the cover message.

In all the above scenarios, a new FI to FI cancellation request (camt.056) case record is created in the system. The system marks the status of this record as CANCELLATIONSENT after the request is sent to the instructed agent of the announcement message. Also, the system marks the status of the customer cancellation record as CANCELLATIONSENT.

This behaviour is the same for both STP and non-STP (Accept) processing.

[Sending FI to FI Cancellation Request to Receiver of Announcement Message and Canceling Original Transaction](#)

If an announcement message has a received positive ACK and a cover is released to a reimbursement agent through clearing or network, it is possible to receive negative ACK or negative DLN for the cover message. If customer cancellation request (camt.055) is received for this scenario, then:

- The system creates an FI to FI cancellation request like camt.056 and sends it to the instructed agent of the announcement message.
- The system marks the status of both the customer cancellation record and FI to FI cancellation record as CANCELLATIONSENT.
- The accounting entries of the transaction are reversed. The transaction status is updated as CANCELLED with cancel reason code marked as FOCR (Following Cancellation Request).
- Pain.002 is sent to the customer based on the customer status report configuration for pain.001.

This behaviour is the same for both STP and non-STP (Accept) processing.

[Sending FI to FI Cancellation Request to Receiver of Cover Message](#)

If an announcement message is sent out and has received positive ACK from network, a cover message is released to clearing or network. Negative DLN received from network for the announcement message. If the system receives a customer cancellation request (camt.055) for this scenario, then it

- Creates an FI to FI cancellation request (camt.056) and sends it to the instructed agent of the cover message.
- Marks the status of both customer cancellation record and FI to FI cancellation record as CANCELLATIONSENT.

This behaviour is the same for both STP and non-STP (Accept) processing.

[Receiving Customer Cancellation Request for Payment with Cancelation Request Already Sent to Clearing/Correspondent Bank](#)

This section details the processing of the customer cancellation request for a payment for which the cancellation request is already sent to clearing or correspondent bank.

**Awaiting Response**

When the FI to FI cancellation request (camt.056) is already initiated by the bank from a cancellation enquiry and is waiting for a final cancellation response, (status of the FI to FI cancelation request is CANCELLATIONSENT), the system rejects the received customer cancellation request.

- The system marks the status of the customer cancellation request as CANCELREJECTED and updates the reason code as NARR (Narrative) with the reason description ‘Cancellation Request already triggered and is waiting for response’.
- The user can see camt.055 and camt.056 records and their statuses from the View Customer Cancellation Request enquiry and also from the Pending and Processed enquiry.

For non-STP processing, the request is parked in the manual queue and on acceptance, the above-mentioned error message is displayed on the screen. The user can send a ‘Pending’ or ‘Reject’ response for this cancellation request.

**Request Accepted**

When FI to FI cancellation request (camt.056) is already triggered by the bank from a cancellation enquiry and has received a positive cancellation response from the other bank or clearing (status of camt.056 is CANCELACCEPTED), the system rejects the received customer cancellation request.

- The system marks the status of the customer cancellation request as CANCELREJECTED and updates the reason code as NARR (Narrative) with the reason description ‘Recall Request already sent and accepted’.
- The user can see camt.055 and camt.056 records and their statuses from View Customer Cancellation Request enquiry and also from Pending and Processed enquiry.

For non-STP processing, the request is parked in the manual queue and on acceptance, the above-mentioned error message is displayed on the screen. The user can send a ‘Pending’ or ‘Reject’ response for this cancellation request.

**Request Rejected**

When the FI to FI cancellation request (camt.056) is already triggered by the bank user from cancellation enquiry and has received a negative cancellation response from the other bank (status of camt.056 is CANCELREJECTED) or has received a negative acknowledgement from the network or has been rejected by the clearing (status of camt.056 is NETWORKREJECTED or CLEARINGREJECTED), then system accepts the received customer cancellation request and forwards the request again to the clearing or the correspondent bank.

- The system marks the status of the customer cancellation request as CANCELLATIONSENT and moves the existing FI to FI cancellation record status from CANCELREJECTED to CANCELLATIONSENT.
- The system updates the newly received values in the camt.056 record and moves the existing values to the history table.
- The user can view all camt.055 and camt.056 records and their statuses from the View Customer Cancellation Request enquiry and also from the Pending and Processed enquiry.

The behaviour is the same for both STP and non-STP processing.
Run OFS.MESSAGE.SERVICE to generate a camt.056 message when the *Generatecamt56forcamt55* field is enabled in `PP.SOURCE`.

[Processing Response for Outgoing FI to FI Cancellation Request Initiated Based on Customer Cancellation Request](#)

This section details the types of responses available for an outgoing FI to FI cancellation request initiated based on a customer cancellation request.

[Positive Response](#)

- On receiving a positive or a partial positive response (camt.029 with CNCL status code) for the outgoing FI to FI Cancellation request (camt.056), the system marks the status of the FI to FI cancellation record as CANCELACCEPTED.
- The system updates the status of the corresponding customer cancellation request as CANCELACCEPTED. The positive ROI response can be followed by a return (pacs.004) or a reject (pacs.002).
- It is also possible to receive a return message before a positive ROI message. In that case, the system marks the status of the FI to FI cancellation record and the corresponding customer cancellation request as CANCELACCEPTED.

[Negative Response](#)

On receiving a negative response (camt.029 with RJCR status code) for the outgoing FI to FI Cancellation request (Camt.056), the system marks the status of the FI to FI cancellation record and the corresponding customer cancellation record as CANCELREJECTED.

[Pending Response](#)

On receiving a pending response (camt.029 with PDCR status code) for the outgoing FI to FI Cancellation request (camt.056), the system retains the status of the FI to FI cancellation record and the corresponding customer cancellation record as CANCELLATIONSENT.

[](#)[Generating Alert on Receiving Response for Outward Cancellation Request](#)

For an outward cancellation request (camt.056) that has received a positive (both accept and partial accept), pending or negative response, the system generates a notification to the client bank based on the configuration in payment order parameter.

TPH publishes this to notify that an outward cancellation request has received a positive, pending or negative response. The notification is triggered in the following scenarios:

- Once an ROI response is received for the cancellation request and status of the cancellation record is updated.
- Once a return message is received as a response for the cancellation request and processed to completed status.

The details sent in the notification are:

| Field Name | Field Details | Remarks |
| --- | --- | --- |
| *Payment Order Reference* | Payment Order ID | Applicable for payment order transactions |
| *Original Payment System Reference* | Transaction reference assigned by customer | Applicable for all responses |
| *Payment System Reference* | Transaction reference assigned by payment system | Applicable for all responses |
| *End to End Reference* | Transaction reference assigned by customer | Applicable for all responses |
| *Message Reference* | Transaction reference assigned by customer/initiating bank | Applicable for all responses |
| *Recall Status* | Status of the recall request | Applicable for all responses |
| *Recall Reference* | Reference number of the recall EBQA ID | Applicable for all responses |
| *Message* | Pacs.004 or Camt.029 message | Applicable for all responses |
| *Credit Account Number* | Account that is credited with the payment amount | Applicable for pacs.004 |
| *Settlement Amount* | The payment settlement amount | Applicable for pacs.004 |
| *Currency* | Currency of the settlement amount | Applicable for pacs.004 |
| *Charge Amount* | Payment Charge amount | Applicable for pacs.004 |
| *Currency* | Currency of the charge amount | Applicable for pacs.004 |
| *Reason Code* | Reason code for the recall response | Applicable for camt.029 response |
| *Reason Description* | Additional Information for recall response | Applicable for camt.029 reject response |

Applicable for all responses indicates both camt.029 and pacs.004

[Viewing Customer Cancellation Request from Enquiry](#)

On receiving a customer cancellation Request for the transaction, the system can display all the received customer cancellation record (camt.055) received from SWIFT and also through the API request in an enquiry along with the statuses and the corresponding original transaction details.

This enquiry is available in **User Menu** > **Payments** > **Payment Hub** > **Investigations and Cancellations** > **Cancellations** > **View Customer Cancellation Requests**.

The user can view the list of all the incoming customer cancellation requests received as a file from network and through API using this enquiry. The user can also use the search criteria to search for any record. The possible user actions are shown in the table below:

| Icon | Name | Description |
| --- | --- | --- |
|  | View EBQA Details | Displays the corresponding customer cancellation record details |
|  | View Orig Txn | Displays the underlying transaction for which the customer cancellation request is received. It opens the transaction in a corresponding ISO view screen. |
|  | View Cancel Req | Displays the received customer cancellation request message (camt.055) in a received XML format. |
|  | View ROI | Displays the generated ROI acknowledgment message to the customer (camt.029 if present) in a XML format. |
|  | View EBQA Details (FI to FI) | Displays the cancellation request sent to the clearing /SWIFT (if present) |

The system exposes this enquiry as an API for the customer to view the status of the cancellation request.

## Processing of Non-payment Messages based on Technical Acknowledgements

When the outward CBPR+ cancellation request (camt.056) or Resolution of Investigation message (Camt.029) or Notice to receive cancellation advice (camt.058) is sent through SWIFT, it is possible to receive negative technical acknowledgements against such non-payment messages. In case of negative technical acknowledgements, these non-payment messages are displayed in the SWIFT ISO Technical Exception enquiry for the user to understand that these have been negatively acknowledged. From the exception enquiry, the system provides an option to Ignore, Accept or resubmit based on the message types (payment/Non Payment).

For non-payment messages, the user can perform actions from the **User Menu** > **Payments** > **Payment Hub** > **Payment Exceptions** > **SWIFT ISO Exception Queue** > **SWIFT ISO Technical Exception** enquiry.

Any action taken by the user for the non-payment messages must be authorized by another user from the **User Menu** > **Payments** > **Payment Hub** > **Payments Approvals** > **Authorize SWIFTISO Exceptions** > **Authorize SWIFTISO Exceptions** enquiry.

When the user performs the Ignore action, no action is taken on the message in Temenos Payments Hub and the user has to take any further action separately outside the system.

- In case a negative acknowledgement is received for a cancellation request (camt.056), system provides following options in Swift ISO technical exception enquiry for the user to take action. The following are the applicable user actions:

| Action | Description |
| --- | --- |
| Ignore | When the user clicks Ignore, no status change happens for the transaction. The message is not listed in exception enquiry on ignore. |
| Resubmit | When the user clicks Resubmit, the same message is resubmitted to the SWIFT network with possible duplicate indicator. |
| Accept | When the user clicks Accept, the system updates the status of the corresponding cancellation request as Network Rejected. The users can view such network rejected outward cancellation requests using the ‘Outward Cancellation Req – Network/Clearing Rejected’ enquiry.  The users can initiate a cancellation request again for the payment from the enquiry below:  **User Menu** > **Payments** > **Payments Hub** > **Payment Investigation and Cancellations** > **Cancellations** > **SWIFT ISO Cancellation** > **Create Cancellation Requests**  Refer to the [Initiating Outward Cancellation Request](#IniOutCan) section for more details about initiation of cancellation request. |

- In case a negative acknowledgement is received against outward Resolution of Investigation message (Camt.029) that is sent as a response for the FI to FI cancellation request (Camt.056) or for camt.058, the system provides following options in Swift ISO technical exception enquiry for the user to take action. The possible user actions are Ignore, Accept and Resubmit.
  - Ignore - Ignores the transaction and does not change its status. This message is no longer listed in the exception enquiry.
  - Resubmit - Resubmits the same message to the Swift network with possible duplicate indicator.
  - Accept - Accepts the transaction and updates the status of the corresponding cancellation request as NETWORKREJECTED.
- In case of negative acknowledgement is received against outward ROI message (Camt.029) that is sent as a response for the customer cancellation request (Camt.055), the system provides the following options in the SWIFT ISO Technical Exception enquiry for the user to take action. The possible useractions are as follows.
  - Ignore – This option only ensures that Camt.029 record does not show in SWIFT ISO Technical Exception enquiry anymore. The system updates the audit trail as NACK ignored from Technial Exception queue by <User ID> on <DateTime>.
  - Resubmit – The system sends the camt.029 message again from the delivery module layer.
- If the outgoing pacs.004 was initiated in response to an incoming camt.056, if a negative DLN or negative ACK is received from Swift network, instead of resending the same message again to the network, user can also decide to accept the response. On accepting, the corresponding EBQA record is updated with status as INWORK and process indicator as MANUAL. The error reason in EBQA table is updated as ‘Return rejected by the network’. So the cancellation request is available for the user to take manual action from the enquiry – 'Inward Cancellation req – Require Manual action'.

Refer to the [Initiating Outward Cancellation Request](#IniOutCan) section for more details about initiation of cancellation request.

## Action on Non-Payments Failing XSD Validation in Temenos Payments Hub Transformation Layer

If non-payment messages such as Resolution of Investigation message (camt.029) or cancellation request (Camt.056) or Notice to receive cancellation advice (camt.058) fails the payload validation in the Camel Transformation Layer, the system updates the audit trail as Payment Failed XSD Validation and displays such payments in the **SWIFT ISO Technical Exception** enquiry. The users can perform one of the following actions on these payments:

| Action | Description |
| --- | --- |
| Ignore | No action is taken in Temenos Payments Hub. Any further action needs to be done manually outside the system |
| Accept | The status of the cancellation message gets updated as NETWORKREJECTED. Refer to the [Recall Processing](#Processing_Payment_Cancellation) section for more information about further processing of cancellation request.  This action is applicable for camt.056 and camt.029. |
| Resubmit | The system displays that the resubmit option is not allowed |

The file status gets updated as Failed along with the error description.

The message with XSD error is still passed to Delivery Camel, but the disposition (status) of the outward messages in DE module is marked as Repair.

## Notification to Receive Cancellation Advice Message

An account owner or a party acting on the account owner's behalf sends the Notification to Receive Cancellation Advice message (camt.058) to one of the account owner's account servicing institutions. It is used to advise the account servicing institution about the cancellation of a notification sent in a previous Notification to Receive message (camt.057).

A notice to receive message is an advance notification from the account owner to their account servicing institution, informing them that the funds will be credited to sender’s account. This notice is sent to the correspondent to pre-advice them of the incoming funds, ensuring that the appropriate values applied for the incoming funds. TPH supports this camt.057 generation for the outward Pacs.009 - bank transfer and for the outward Pacs.009 - own account transfer as well.

camt.057 generation is currently not supported for customer transfer so camt.058 generation is also not supported.

Read [PPSWMX - Notification to Receive](../PPSWMX/Introduction.htm) section for more details about the Notice to receive (camt.057) message.

### Initiation of camt.058 for camt.057 using an Enquiry

A enquiry named Notice to Receive cancellation advice is available for the user to initiate the camt.058, for camt.057 message. This enquiry is present under the below navigation:

User Menu > Payments > Payment Hub > Investigations and Cancellations > Cancellations > SWIFT ISO Cancellations> Create Cancellation Request > Create Cancellation Advice for Notice to Receive.

This enquiry lists all the bank transfer messages for which the notice to receive (camt.057) is already generated. For the bank transfer message, if the camt.057 has received the negative acknowledgement or negative delivery notification from the SWIFT network, then the user cannot initiate the camt.058 in such scenarios. So those records are not displayed in this enquiry.

Only the eligible records for initiating the camt.058 are displayed here. The user can perform the following actions:

| Action | Description |
| --- | --- |
| View | System displays the payment details in ISO screen |
| View in Details | System displays the view in details page for each record from which user can view the outgoing messages (Pacs.009 and camt.057) |
| Cancel Notice to Receive | User can initiate the cancellation request for the camt.057 using this icon. |

Clicking the Cancel Notice to Receive icon to open the new version for the user to input the details for initiating the cancellation request. The user can input the *Cancel Originated By* field with the values as B (bank) or C (customer) and select the required cancel reason code for initiating cancellation request and optionally provide the additional information for the same. When the originator is selected as:

- Customer - Then the original debtor of the underlying transaction (Pacs.009) is populated as the Originator of camt.058 in the outward message.
- Bank - Then the processing company BIC is populated as the originator of camt.058 in the outward message.

[System Validation - Initiating camt.058](#)

- Processing bank should be SWIFTMX enabled (that is, COMPANY.PROPERTIES >> SWFMXEffectiveDate should be configured with the date less than or equal to the current processing date). If the bank is not SWIFT MX enabled, then the system displays an error: Cannot create cancellation request since the company is not MX enabled.
- The output channel of the underlying transaction should have the clearing transaction type and the outward message type configured in the clearing configuration. If not, the system throws an error: Notice to receive cancellation is not allowed for the clearing or network.
- There should not be any duplicate cancellation request already triggered for the same record. If there is a duplicate cancellation request, then the system displays an error Cancellation Request already triggered.
- If the already triggered cancellation request is in NETWORKREJECTED status, then the same record is opened for user modification.
- The system checks if RMA is present between the TPH bank and the receiver of the camt.058. if RMA is not present, then the system throws an error: RMA not available with assignee or receiver for sending camt.058.
- The system checks if the additional information is provided by the user for the cancel reason code as NARR. If not provided, then system displays an error ‘Additional information must be provided for reason code NARR’.

Once all the validations are successful, then the record is submitted and moved for authorisation. An authoriser can verify the record from the below navigation.

User Menu > Payments > Payment Hub > Investigations and Cancellations > Cancellations > SWIFT ISO Cancellations > Create Cancellation Request > Authorise Cancellation Advice for Notice to Receive.

Once authorised, a cancellation request (camt.058) is created and sent out to the receiver of the camt.057 through the delivery layer.

[Automatic Initiation of camt.058 along with camt.056](#)

Once pacs.009 and camt.057 are generated and sent out, pacs.009 is sent to the correspondent bank and the camt.057 is sent to the creditor agent bank. In certain scenarios, the bank transfer is rejected or returned by the correspondent bank due to a cancellation request or for other functional reason, but the creditor agent is never notified about the fund’s status.

The creditor agent might credit the creditor based on the notice to receive message. To avoid this, when the user initiates the FI-to-FI cancellation request (camt.056) for bank transfer or for own account transfer from TPH bank, camt.058 (Notice to receive cancellation advice) should also be generated automatically to the creditor agent.

In this scenario, camt.056 cancellation request is generated for pacs.009 and camt.058 cancellation request is generated for camt.057.

[System Validation - Initiating camt.056 and camt.058 Together.](#)

The following validations are performed for camt.058 while initiating the FI-to-FI cancellation request (camt.056) for bank transfer when camt.057 is already generated. Existing validations of camt.056 continues. The system:

- Performs a duplicate check: (that is, if camt.058 is already generated for camt.057). If it is a duplicate request, the system displays an override: 058 is already triggered so camt.058 will not be generated. On accepting the override, only camt.056 is generated.
- Performs RMA check (that is, if RMA is present between TPH bank and the receiver of camt.058 for sending cancellation request). If no RMA, the system displays an override: RMA not available with assignee or receiver for sending camt.058, so camt.058 will not be generated. On accepting the override, only camt.056 gets generated.
- Checks if the required clearing configuration is present to send the camt.058 (that is, a clearing configuration check) if clearing configuration is not present, then the system displays an override: Notice to receive cancellation (camt.058) is not allowed for the clearing or network, so camt.058 will not be generated. On accepting the override, only camt.056 is generated.
- Checks if the camt.057 which is already generated has received negative ACK, negative dln or xsd failure (NAK or Negative dln check). If there are any errors for camt.057, then an override is displayed: Notice to receive camt.057 has received negative ACK/DLN, so camt.058 will not be generated. On accepting the override, only camt.056 is generated.

Once all the validations are successful, camt.056 and camt.058 are generated and sent to the SWIFT network through the delivery layer. In this automatic generation of camt.058, the reason code is defaulted as Entry no longer expected (NOLE) and the *Additional Information* field is left blank. The system defaults the originator tag of camt.058 with the processing company BIC details.

[ACK or NAK Processing for camt.058](#)

Read [Processing of Non-Payment Messages based on Technical Acknowledgements](#ProcessNonPayment) for information on ACK/NAK processing of camt.058.

In this topic

- [Introduction to SWIFT MX Cancellations and ROI](#IntroductiontoSWIFTMXCancellationsandROI)

- [Message Types](#MessageTypes)
- [Payment Cancellation Processing](#PaymentCancellationProcessing)
- [Processing Customer Payment Cancellation Request](#ProcessingCustomerPaymentCancellationRequest)
- [Processing of Non-payment Messages based on Technical Acknowledgements](#ProcessingofNonpaymentMessagesbasedonTechnicalAcknowledgements)
- [Action on Non-Payments Failing XSD Validation in Temenos Payments Hub Transformation Layer](#ActiononNonPaymentsFailingXSDValidationinTemenosPaymentsHubTransformationLayer)
- [Notification to Receive Cancellation Advice Message](#NotificationtoReceiveCancellationAdviceMessage)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:47:39 PM IST
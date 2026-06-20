# Introduction to Liquidity Transfer Requests

> Source: https://docs.temenos.com/docs/Solutions/Payments/Payments/LQ/Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Request/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Liquidity Transfer Request > Introduction

- Liquidity Transfer Advice;)
- Liquidity Transfer Request;)
  - [Introduction](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Request/Introduction.htm)
  - [Configuration](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Request/Configuration.htm)
  - [Working with](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Request/Working_with.htm)
  - [Tasks](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Request/Tasks.htm)
  - [Outputs](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Request/Outputs.htm)

Payments

# Introduction to Liquidity Transfer Requests

Updated On 22 March 2025 |
 13 Min(s) read

Feedback
Summarize

Liquidity Transfer Requests (LTR) are instructions that are raised by participant banks to transfer funds between two accounts held by an Account Holding Institution (AHI). AHIs are typically clearing system, for example TARGET2, TARGET Instant Payment Settlement (TIPS), EBA Real Time payment infrastructure platform by Euro Banking Association (RT1), and so on. The participant banks can move funds between accounts to which they have required access. The purpose of an LTR is to increase the balances or position of an account to meet its obligations, or decrease the balance or position of an account when there is surplus. These transfers enable the account holder bank to manage settlement obligations and liquidity effectively for their payments operational requirements every day.

The Treasury department of the bank initiates liquidity transfers for one of the following reasons:

- Balance transfers between settlement accounts of the bank within the AHI, or from/to bank’s indirect participants.
- Sub-account top-ups (instant clearing position accounts) and withdrawals.
- Balance transfers to or from another participant’s settlement account within the same liquidity group.
- Funding the technical accounts maintained with clearing to fulfil obligations arising from day-to-day inter-bank clearing requirements.
- Liquidity adjustment movements
- Release and withdrawal of intra-day liquidity (based on the security held by the bank at securities settlement system), and repo repayments to Central bank.

In Temenos Payments Hub , the user can capture LTRs from the LTR screen of the PAYMENT.ORDER (PO) application or the Order Entry LTR Graphic User Interface (GUI). Upon successful processing, the system posts the accounting entries and sends a liquidity credit transfer message to the clearing network. While Temenos Payments Hub uses internal accounts to perform posting, their equivalent external accounts (also called as market accounts) are furnished in the outgoing LTR request to clearing.

Clearing responds to the liquidity credit transfer message with a business acknowledgement message to indicate whether the LTR is accepted or rejected. On receipt of a negative response, based on the configuration, either a reversal payment is booked against the original LTR or the LTR is moved to an exception queue from where the user can manually act on it.

## Capturing LTR

The user can capture LTRs from the LTR GUI of the PO application and the LTR GUI of the OE screen, as follows.

- To capture an LTR from the PO application, navigate to **User Menu** > **Payments** > **Liquidity Management** > **Front Office** > **LTR Initiation**.
- To capture an LTR from the OE screen, navigate to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **LTR Initiation**.

The user captures the following fields.

| Fields | Description |
| --- | --- |
| *Payment Order Product* | Applicable only in the LTR screen of the PO application. The user can select the product relevant to the channel using which the LTR message is delivered |
| *Debit Account Number* | Indicates the account number (as maintained in the bank’s books) that is debited. The user can manually select the account number.  When this field is left blank, it is auto-populated when the *External Debit Account* field is captured based on the internal-external account mapping |
| *Debit Account Currency* | Indicates the currency of the debit account number |
| *Debit Account Name* | Indicates the name of the debit account number |
| *External Debit Account* | Indicates the account number (as maintained in the account holding institution) that is debited. The user can manually select the account.  When this field is left blank, it is auto-populated when the *Debit Account Number* field is captured, based on the internal-external account mapping |
| *Payment Currency* | Indicates the transaction currency |
| *Payment Amount* | Indicates the transaction amount |
| *Credit Account Number* | Indicates the account number (as maintained in the bank’s books) that is credited. The user can manually select the account.  When this field is left blank, it is auto-populated when the External Credit Account field is captured, based on the internal-external account mapping |
| *Credit Account Currency* | Currency of the credit account number |
| *Credit Account Name* | Name of the credit account number |
| *External Credit Acc*ount | Indicates the account number (as maintained in the account holding institution) that is credited. The user can manually select the account.  When this field is left blank, it is auto-populated when the *Credit Account Number* field is captured, based on the internal-external account mapping |
| *Local Instrument Code* | Indicates the Clearing-specific codes. The LTR message type is selected based on the input of this attribute. When the user captures this field as "SBTI", the system generates a pacs.009 LTR message. For all other local instrument codes, the system generates a camt.050 LTR message |
| *Output Channel* | The user can select the output channel using which the LTR message is to be delivered. Applicable only in the LTR OE screen. |

## Processing Liquidity Transfer Request

In addition to normal payment processing, the captured LTRs are subject to liquidity management specific processing, as follows:

| Process | Description |
| --- | --- |
| Account Derivation | External account numbers are account numbers as maintained with the AHI. Internal account numbers are account numbers that are maintained in the participant bank’s books. These in-house accounts are typically mirror accounts to the external accounts and can either be a Nostro or a suspense account. During LTR initiation, the user can capture either internal accounts or the external accounts. When the user captures internal accounts, the external accounts are auto-populated and vice-versa. The internal to external account mapping can be configured from the menu under **Admin Menu** > **Payments** > **Liquidity Management** > **LTA Account Mapping**. |
| Service Derivation | Certain clearing systems such as TARGET2 have multiple services, for example - TARGET2 CLM (Central Liquidity Management) and TARGET2 RTGS (Real-Time Gross Settlement). TARGET2 CLM holds the Main Cash Accounts (MCA) and TARGET2 RTGS holds other accounts such as Dedicated Cash Account (DCA), sub-accounts, and so on. The system sends the LTR message to the service that holds the account being debited. Temenos Payments Hub derives the service based on the ‘Account Residing Service’ configuration in the LQ.ACCOUNT.MAPPING (liquidity management account mapping) table. |
| Message Derivation | Certain clearings support multiple liquidity transfer message types. Temenos Payments Hub derives the message type to be generated based on the Local Instrument Code (LIC) in the captured LTR payment.  TARGET2 supports both camt.050 and pacs.009 LTR message types. The system generates a pacs.009 LTR message and sends it to TARGET2 when the user captures the LIC as ‘SBTI’. For all other cases, the system generates a camt.050 and sends it to TARGET2. |

## Viewing LTR using LTR Enquiry

The user can view the booked liquidity transfer requests in a separate GUI. The user can enquire the LTR based on various criteria such as Transaction Reference Number, Payment Amount, Payment Currency, Debit Account, Credit Account, LTR status, and so on.

To open the LTR enquiry in the PO application, go to **User Menu** > **Payments** > **Liquidity Management** > **Front Office** > **LTR Enquiries**.

To open the LTR enquiry in Temenos Payments Hub , go to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **LTR** > **Enquiries** > **View LTR Payments**.

## Processing LTR from Repair Queue

When the system is unable to process an LTR due to reasons such as validation failures, the system parks the payment in the repair queue.

To view LTRs that are in repair, go to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **LTR** > **Exceptions** > **LTR Repair Queue**.

From the repair screen, the user can either cancel the LTR or modify it to process the payment. When the user opts to repair the LTR, the user can edit the following fields:

- *Debit Account Number*
- *Debit Currency*
- *External Debit Account*
- *Processing Date*
- *Output Channel*
- *Local Instrument Code*
- *Credit Account Number*
- *Credit Currency*
- *External Credit Account*

When the user cancels the LTR from the repair queue, the payment moves to a final Cancelled status after the supervisor’s authorisation. The user has to enter the reason for the cancellation.

If the user opts to repair the LTR and after necessary modifications, the user has to click the Validate icon and the Submit icon to validate the input and submit the LTR. The system re-validates the LTR to ensure that functional errors are cleared and new errors does not exist. After the supervisor’s approval, the repaired LTRs are moved back for processing.

## Viewing and Processing Liquidity Transfer Requests from Exception Queue

Based on the content of the LTR message received from the participant bank, the clearing sends a technical and/or business response to the participant bank confirming the acceptance or rejection of the LTR. The following sections explain the actions that are possible on receiving a reject response from clearing.

[LTR Technical Exception Queue](#)

LTRs that are generated and sent to clearing, and receives a negative technical acknowledgement or are awaiting a positive acknowledgement are moved to the ‘LTR Technical Exception Queue’. To view the LTRs, go to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **LTR** > **Exceptions** > **LTR Technical Exceptions**.

The system parks an LTR in this queue for the following reasons:

- Receipt of a technical negative acknowledgement (nack) from the network
- Receipt of a failed delivery notification (DLN)
- Receipt of a negative acknowledgement from the gateway (admi.007)
- Awaiting a positive acknowledgement (ack)

Not all clearing networks support the above features. Moving the LTR to the technical exception queue is dependent on whether the clearing network supports the features and if the participant bank is subscribed to the feature. For example, if a clearing network does not send an acknowledgement for the LTR sent by the participant bank, then the payment does not move to the technical exception queue.

[LTR Business Exception Queue](#)

Clearing performs various business validations as part of the LTR settlement process and then tries to settle the payment. Based on the status of validation and settlement, the clearing sends a business acknowledgement.

TARGET2 sends a pacs.002 against a pacs.009 LTR and a camt.025 against a camt.050 LTR to indicate of the status of the settlement.

- If the settlement fails or is rejected, the clearing sends a negative business acknowledgement to the participant bank that sent the LTR message.
- If the settlement is successful, a positive acknowledgement is sent to the sending participant bank.

If the bank receives a positive business acknowledgement, the system updates the audit trail of the underlying LTR, and the status remains completed. If the bank receives a negative business acknowledgement, the system can be configured to process the acknowledgement either in Straight Through Processing (STP) mode or manually. If the user configures manual processing, then the user can view all such LTR payments in the LTR Business Exception Queue enquiry for manual action.

To access the LTR Business Exception Queue enquiry, go to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **LTR** > **Exceptions** > **LTR Business Exceptions**.

The enquiry provides the following actions:

| Action | Description |
| --- | --- |
| Reverse | Temenos Payments Hub posts a reversal transaction and moves the payment status to 993 (reversed). |
| Ignore | The transaction remains in Completed status and does not post any reversal accounting entries. |

In this topic

- [Introduction to Liquidity Transfer Requests](#IntroductiontoLiquidityTransferRequests)

- [Capturing LTR](#CapturingLTR)
- [Processing Liquidity Transfer Request](#ProcessingLiquidityTransferRequest)
- [Viewing LTR using LTR Enquiry](#ViewingLTRusingLTREnquiry)
- [Processing LTR from Repair Queue](#ProcessingLTRfromRepairQueue)
- [Viewing and Processing Liquidity Transfer Requests from Exception Queue](#ViewingandProcessingLiquidityTransferRequestsfromExceptionQueue)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:21:25 PM IST
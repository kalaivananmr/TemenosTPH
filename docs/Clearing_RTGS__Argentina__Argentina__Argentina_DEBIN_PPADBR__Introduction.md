# Introduction to DEBIN Registration Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Argentina/Argentina/Argentina_DEBIN_PPADBR/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Argentina > DEBIN Registration Clearing > Introduction

- Argentina;)
  - DEBIN Registration Clearing;)
    - [Introduction](../../Argentina/Argentina_DEBIN_PPADBR/Introduction.htm)
    - [Configuration](../../Argentina/Argentina_DEBIN_PPADBR/Configuration.htm)
    - [Working with](../../Argentina/Argentina_DEBIN_PPADBR/Working_with.htm)
    - [Tasks](../../Argentina/Argentina_DEBIN_PPADBR/Tasks.htm)
    - [Outputs](../../Argentina/Argentina_DEBIN_PPADBR/Outputs.htm)
  - CT & DD (ACH) Clearing;)
  - Instant Clearing;)

Payments

# Introduction to DEBIN Registration Clearing

Updated On 22 March 2025 |
 12 Min(s) read

Feedback
Summarize

DEBIN is an immediate online transfer service using which the beneficiary (for example, seller) initiates the payment request and the payer (for example, buyer) accepts or rejects the received request. Once the request is accepted, it debits the funds from the payer’s (buyer) account and credits to the beneficiary (seller) account by using COELSA (clearing house for DEBIN payments).

This module covers the following interface or regulation version:

- DEBIN Regulation Version 3.0.5.

The BCRA (Central Bank of Argentina Republic) appointed the Compensating Chamber of Low Value (COELSA), which is under the direct regulation of the monetary authority, acts as administrator of all DEBIN operations.

The parties (buyer and seller) need to be registered as DEBIN participants with COELSA to use the DEBIN service. The DEBIN workflow is as follows:

1. Beneficiary initiates a debit request (DEBIN order) from any channel to the bank.
2. Bank generates the order of DEBIN, registers the minimum data, and sends the request to COELSA.
3. Payer’s bank receives the DEBIN request through COELSA and sends DEBIN notification to the customer.
4. Payer confirms the transaction and verifies the balance. If feasible, it debits the amount and communicates to COELSA.
5. Beneficiary bank credits the beneficiary account once it receives the communication from COELSA.

The below diagram depicts the flow of messages between Temenos Payments Hub banks (buyer or seller bank or both) and COELSA.



Any communication between the creditor and debtor bank is done through COELSA.

DEBIN admits payments in Argentinian pesos (ARS) or dollars (USD), only between accounts of the same currency. DEBIN also have an expiry time and requests accepted by the payer after the expiry time will be rejected by COELSA (clearing house for DEBIN payments).

The DEBIN validity period can be from 10 minutes to 72 hours. This time will be selected by the seller while initiating the request.

New statuses for DEBIN payments will be updated in the Temenos Payments Hub for each payment type.

## Debit Order Application

The PPADEB.DEBIT.ORDER application is introduced to capture the payment requests initiated by the seller.

- It captures the payment with *Direction* as ‘Outward’ and sends it to clearing (COELSA).
- COELSA transmits the payment requests to the respective buyer bank. The incoming requests are also captured in the same application with *Direction* as ‘Inward’.
- To execute the payment, the buyer in the order needs to perform one of the following:
  - If the buyer rejects the request, it is cancelled.
  - If buyer accepts the request, it is routed to Temenos Payments Hub through PAYMENT.ORDER(PO) application and the following occurs:
    - Initiates an outgoing Credit Transfer (CT) in Temenos Payments Hub
    - Debits the buyer account
    - Credits the clearing suspense account
    - Moves the status of the payment in Temenos Payments Hub to 687 (awaiting acknowledgement)
- Subsequently, COELSA sends an acknowledgment to the buyer bank with response ‘OK’ or ‘Not OK’.
  - If ‘OK’, the transaction is considered completed and the status is moved to 999 (Completed).
  - If ‘Not OK’, the transaction is reversed and the buyer’s account is credited with the transaction amount and the status is moved to 998 (Reversed).
- At seller’s bank side, this instruction comes as an incoming CT and the bank credits the seller’s account.

The PPADEB.DEBIT.ORDER,INITIATION version allows users to input the COELSA *Recurrence Id* when initiating a debin order payment.

## DEBIN Registration

The PPADBR.DEBIN.REGISTRATION application is used for DEBIN registration. When a customer (buyer or seller) approaches the Temenos Transact bank for registration, the below details are captured in the new table and sent to COELSA for confirmation.

The *Role* field in the table identifies whether the customer is registering as Buyer or Seller.

The following details are captured in the table:

- *Legal* *Document Number*
- *Account* *(CBU)* *Number*
- *Customer Bank Code* (defaulted from first three positions of 'Account CBU Number')
- *Customer Branch Code* (defaulted from forth to eighth position of 'Account CBU Number')
- *Customer Email Information*

During registering, the customer can enter the auto-acceptance conditions by providing values in the *Auto Accept Ccy* and *Auto Accept Amt* fields. Once the record is committed, the system sends an IF event with all the details of the record (which is consumed by L2 layer) to move the message to COELSA.

| Activity | Description |
| --- | --- |
| DEBIN Deregistration | - To deregister from DEBIN service, set the *Action* field to ‘Deregister’ in PPADBR.DEBIN.REGISTRATION. Only an active record can be deregistered. - It also provides an enquiry to the customer to list the active DEBIN registrations with an option to deregister. - On selecting the ‘De-Register’, an underlying page of the DEBIN registration record with *Action* field defaulted as ‘De-Register’ is displayed. - Once the record is committed, the system sends an IF event with all the details of the record (which is consumed by L2 layer) to move the message to COELSA. |
| Status update by L2 layer | On successful deregistration (that is, positive acknowledgment is received from COELSA), the status of the record is updated to ‘Deleted’. If a negative acknowledgement is received, the *Status* remains ‘Active’ and the participant has to deregister again. |
| DEBIN Reactivation | - To reactivate  DEBIN registration after deregistering, set the *Action* field to ‘Re-activate’ in PPADBR.DEBIN.REGISTRATION. Only a deleted record can be re-activated. - It also provides an enquiry to the customer to list the deleted DEBIN registrations with an option to reactivate. - On selecting the ‘Re-activate’, an underlying page of the DEBIN registration record with *Action* field defaulted as ‘Re-activate’ is displayed. - Once the record is committed, the system sends an IF event with all details of the record (which is consumed by L2 layer) to move the message to COELSA. |
| Status update by L2 layer | On successful reactivation (that is, positive acknowledgment is received from COELSA), the *Status* of the record is updated to ‘Active’. If a negative acknowledgement is received, the *Status* remains ‘Deleted’ and the participant has to reactivate again. |

## Seller Limit Definition

After registration, a seller can set limits. Limits have to be entered in both USD and ARS currency by using the same DEBIN registration table (PPADBR.DEBIN.REGISTRATION) by setting the *Action* field to ‘Set Limits’.

Once the record is committed, the system sends an IF event with all details of the record (which is consumed by L2 layer) to move the message to clearing (COELSA).

Limit details are maintained in COELSA and no check or validation is done in Temenos Transact.

## Recurrence Registration

A seller or buyer can initiate recurrence (opt-in) registration request to each other. On registering recurrence between seller and buyer, an upcoming DEBIN order initiated by the seller is auto accepted at the buyer’s end.

This recurrence registration (opt-in) request can be initiated either by the seller or buyer. Once initiated, the other party has to accept it. There is no option to reject this request. However, the other party can dropout of the registered recurrence post registration.

| Request Type | Description |
| --- | --- |
| Opt-in | Both the buyer and seller can initiate an ‘Opt-in to recurrence’.  - If the buyer initiates, their entity sends an opt-in to recurrence to COELSA. COELSA registers it and gives notice to the entity of the seller. - If a seller initiates, the seller’s bank sends the opt-in to COELSA and buyer’s entity is notified. |
| Dropout | The seller or buyer can dropout of the registered recurrence by initiating a dropout request to COELSA.  All the details applicable for opt-in request are required for dropout request with *Action* field set as ‘False’.  Only active recurrence records can be used to initiate dropout. The other party (either buyer or seller) cannot accept or reject a record. It is accepted by default. |

[Recurrence Status Update](#)

DEBIN allows banks to transfer funds between customers with an immediate transfer. Unlike other means of payment, DEBIN is an immediate online transfer by which the collector initiates the process and the payer has to accept it. DEBIN admits payments in Argentinian pesos (ARS), only between accounts of the same currency. DEBIN also has an expiry time and the requests accepted by the payer after the expiry time will be rejected by COELSA.

This functionality allows banks to receive the 5013 response code from COELSA when the DEBIN recurrence is active, available, or registered with the Clearing. Temenos Payments Hub will receive the 5013 response code and will update the *Recurrence Status* field as Active instead of Rejected in the PPADBR.RECURRENCE.REGISTRATION application.

### Recurrence Details

An enquiry is provided to list the active or inactive recurrences from system table. To get the updated details from COELSA, bank operators can use PPADBR.RECURRENCE.DETAILS.COELSA enquiry. As part of this request, CUIT of seller and buyer along with CBU of buyer is sent to COELSA. It updates the response received from COELSA in the registered recurrence list and table.

Additionally, another enquiry is available to view only the seller details with active recurrences. Similarly, to get the updated details from the COELSA, it sends the seller CUIT to COESLA and updates the details from clearing to the recurrence table.

### Chargeback

Buyer can initiate chargeback for the pre-authorised DEBIN payment.

- On initiating the chargeback, the request is sent to COELSA.
- On receiving the positive response, the reversal is initiated for original transaction at Temenos Payments Hub.

Once the payment is reversed, debit order status is updated accordingly. This chargeback notification is forwarded to the seller bank and cannot be rejected as it is already validated by COELSA.

The same process is followed to reverse transactions at seller’s end.

## DEBIN Archival

The functionality allows banks to archive the payments after the retention period.

The following items are introduced as part of this functionality:

- The **View Debit order History** menu allows users to view the list of history files for DEBIN orders.
- The **View Debit order Archived** menu allows users to view the archived debit orders.
- The PPADEB.DEBIT.ORDER.PRODUCT application allows users to set the *Retention Period* after which the Debin orders to be moved from live to history.
- The ARCHIVE application allows users to set the *Retention Period* after which the Debin orders to be moved from history to archive.

## Illustrating Model Parameters

Read the [Temenos Payment (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Initiation (PI)](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm) user guide for information on parameter setup for Argentina clearing.

## Illustrating Model Products

This module provides the facility to send and receive Argentina Clearing Payments from COELSA clearing.

In this topic

- [Introduction to DEBIN Registration Clearing](#IntroductiontoDEBINRegistrationClearing)

- [Debit Order Application](#DebitOrderApplication)
- [DEBIN Registration](#DEBINRegistration)
- [Seller Limit Definition](#SellerLimitDefinition)
- [Recurrence Registration](#RecurrenceRegistration)
- [DEBIN Archival](#DEBINArchival)
- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)

Related topics:

- [Temenos Payments Hub](../../Payments_Hub_(PP)/Misc/Introduction.htm)
- [Payments Initiation](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm)
- [Temenos Payment Services](../../Services/Misc/Services.htm)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:51:39 PM IST
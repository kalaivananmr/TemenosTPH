# Working with DEBIN Registration Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Argentina/Argentina/Argentina_DEBIN_PPADBR/Working_with.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Argentina > DEBIN Registration Clearing > Working with

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

# Working with DEBIN Registration Clearing

Updated On 23 May 2023 |
 32 Min(s) read

Feedback
Summarize

This section helps the user to understand the working of DEBIN.

## DEBIN Registration

Customer can register for DEBIN service by giving the mandatory fields along with the *Role* as Buyer or Seller.

The following fields are mandatory: *Customer ID*, *CUIT* and *CBU* *Account Number*.

1. To access DEBIN registration, go to **DEBIN.REGISTER.MENU**.
2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Auto* *Accept Ccy* and *Auto Accept Amt* | Defines the auto-acceptance criteria. |
   | *Action* | Allows the following values: - To deregister the active registration, select ‘Deregister’. - To reactivate the deleted registration, select ‘Reactivate’. - To set the seller limits, select 'Setlimits'. |



[Example](#)

The buyer registers with the following auto-acceptance conditions:

- The allowed amount for incoming request from seller SEL123123456 is ARS 5,000. The ARS 5,000 requires manual confirmation.
- The allowed amount for incoming request from any seller is USD 10,000. There is no definition for ARS currency. Hence, any incoming request in ARS (except for seller SEL123123456) requires manual confirmation.



If a DEBIN request does not qualify for auto-approval, Temenos Transact does not notify the end user (buyer) to accept or reject the transaction.

## Recurrence Registration

The following are the two options available for recurrence registration:

| Option | Description |
| --- | --- |
| Opt-in | A seller or buyer who has an active DEBIN registration can request for opt-in. This request is sent to COELSA and forwarded to the other end (buyer or seller).  - To initiate opt-in request, enter the mandatory fields in the ‘Create Opt-in Recurrence Request’ registration version. - On receiving the positive response from COELSA, the *Recurrence Status* of the record is changed to ‘Active’.   This recurrence registration and debit order can be accessed from PPDEBIN menu. |
| Dropout | A seller or buyer who does not want recurrence registration, can request for a dropout.  - A drop-out request is sent to COELSA - On receiving the positive response from COELSA, the *Recurrence Status* of the record is changed to ‘Inactive’. |

[](#)[Enquiry to View Registered Recurrences](#)

To view all registered recurrences, launch the DEBIN application and go to **View recurrence details**>**Recurrence details of Seller and Buyer**.



[Recurrence Status Update](#)

The workflow for this functionality is displayed below.



The recurrence request is the authorisation between parties, which can be initiated by both seller and buyer. Once initiated, the other party bank will auto-accept the recurrence request. There is no option to reject this request.

The following statuses are available for the recurrence:

- Active: When Temenos Payments Hub receives the 5000, 5013 response codes from COELSA.
- Inactive: When Temenos Payments Hub receives the 5050 response code from COELSA.
- Rejected: All other response codes received from COLESA are changed as Rejected.

COELSA validates the recurrence registration request and sends the acknowledgement along with the response code and description to the bank.

Once the acknowledgement is received, based on the response code, the *Recurrence Status* field is updated in Temenos Transact.

As per the process flow, the recurrence is registered by the seller or buyer. If both buyer and seller are registering for the DEBIN recurrence, the second person is getting the response code as 5013 from COELSA, as this recurrence is already available with the Clearing. Temenos Payments Hub receives the 5013 response code from Clearing and updates the *Recurrence Status* field as Active in the PPADBR.RECURRENCE.REGISTRATION application.

[Initiate the Recurrence Registration as a Seller](#)

In this scenario, a seller is successfully registered for the recurrence, using the Opt-In option. COELSA sends the 5000 response code to the registering bank and a notification to the other bank. The buyer also tries to register for the same recurrence with the seller by mistake or without checking the notification. The buyer bank receives the 5013 response code from Clearing.

1. COELSA sends a response code as 5000, for the new registration.


2. The *Recurrence Status* is sent as Active. Once the recurrence registration is done, the buyer is notified but without seeing the notification, the buyer also tries to register for the recurrence with the same Id.
3. COELSA sends the response code as 5013 (existent) so that the *Recurrence Status* for the buyer is set as Active in the PPADBR.RECURRENCE.REGISTRATION application.



[Initiate the Recurrence Registration as a Buyer](#)

In this scenario, a buyer is successfully registered for the recurrence, using the Opt-In option. COELSA sends the 5000 response code to the buyer bank and a notification to the seller bank. The seller also tries to register for the same recurrence with the buyer by mistake or without checking the notification. The seller bank receives the 5013 response code from Clearing.

1. COELSA sends the response code as 5000, for the new registration.
2. The *Recurrence Status* is sent as Active. Once the recurrence registration is done, the seller is notified but without seeing the notification, the seller also tries to register for the recurrence with the same Id.
3. COELSA sends the response code as 5013 (existent) so that the *Recurrence Status* for the seller is set as Active in the PPADBR.RECURRENCE.REGISTRATION application.



[Incoming Recurrent DEBIN](#)

When DEBIN is processed automatically as expected and Temenos Transact tries to inform COELSA accordingly (COELSA response exists), the DEBIN status is moved to In Progress and a positive acknowledgement (OK) is received from COLESA so that the status is moved to Credited. If a negative acknowledgement (NOT-OK) is received from COLESA, Temenos Payments Hub changes the status to Data Error.

When DEBIN is processed automatically as expected and Temenos Transact tries to inform COELSA accordingly (COELSA response does not exist), the DEBIN status is moved to In Progress and a positive acknowledgement (OK) is received from COLESA so that the status is moved to Credited. If a negative acknowledgement (NOT-OK) is received from COLESA, Temenos Payments Hub changes the status to Data Error. If there is no response received from clearing after the configured retry, the recurrent DEBIN is moved to Debit Error.

When an incoming recurrent DEBIN is received and the COELSA response exists but COELSA notifies about an issue while crediting the seller (buyer side), the DEBIN status is moved to In Progress and a positive acknowledgement (OK) is received from COLESA so that the status is moved to Credited. After the SLA configured by the clearing house, there is a rejection request to revert the payment. After this time, Temenos Transact moves the DEBIN to Credit Error and the payment is reversed.

When an incoming recurrent DEBIN is received and the COELSA response exists) but there is an issue inside the Temenos Payments Hub flow, the DEBIN status is moved to In Progress due to a validation failure (FCM hit, posting restrictions, etc). Temenos Payments Hub will send to COELSA the 30 - Otros problemas con la cuenta de Débito message. If a positive acknowledgement (OK) response is received from COELSA, the status is moved to Debit Error. If a negative acknowledgement (NOT-OK) is received from COLESA, the DEBIN status is moved to Data Error.

When Temenos Transact tries to start the automatic debit with incorrect data in any of the JSON fields of /AvisoDebinPendiente (CUITs, CBUs, ALIAS, time zone etc.), the DEBIN file level validation is failed and the proper error code is sent to the clearing house (40 - Otros problemas). Once the acknowledgement is received, Temenos Transact moves the DEBIN order to Data Error. It is assumed that the negative acknowledgement (NOT-OK) will be received from clearing. If there is still no response from clearing, the retry will happen and then, the DEBIN will be moved to Debit Error.

When an incoming recurrent DEBIN is processed automatically as expected, the DEBIN status is moved to In Progress due to a validation failure (due to insufficient funds) from Initiated. The 20 - Sin saldo en la cuenta message is sent to COELSA. If a positive acknowledgement (OK) response is received from COELSA, the status is moved to Insufficient Funds. If a negative acknowledgement (NOT-OK) is received from COLESA, Temenos Payments Hub changes the status to Data Error. If there is no response received from COELSA in the stipulated or configured time, the retry will be done and if still there is no response from COELSA, the DEBIN payment is moved to the Debit Error status. No further action is required.

[Scenario 1](#)

In the following example, an incoming recurrent DEBIN (buyer) is created and a positive acknowledgement (OK) is received from COELSA.

1. The following OFS message is processed to create a DEBIN order.


2. A DEBIN order has been created and it can be checked in the PPADEB.DEBIN.ORDER application.


3. Initially, the DEBIN order is in the In-progress *Status*.
4. The payment is created in status 4.
5. After running the BNK/PAYMENT.STPFLOW.MEDIUM service, the payment moves to status 687.


6. The following OFS message is processed.


7. The payment moves to status 999.


8. The *Status* of the DEBIN order is updated as Credited.



[Scenario 2](#)

In the following example, an incoming recurrent DEBIN (buyer) is created. After the SLA configured, the payment is reversed due to a cancellation request and the DEBIN order is moved to the Credit Error status.

1. The following OFS message is processed to create a DEBIN order.


2. A DEBIN order has been created and it can be checked in the PPADEB.DEBIN.ORDER application.


3. Initially, the DEBIN order is in the In-progress *Status*.
4. The payment is created in status 4.
5. After running the BNK/PAYMENT.STPFLOW.MEDIUM service, the payment moves to status 687.


6. The following OFS message is processed.


7. The payment moves to status 999.


8. The *Status* of the DEBIN order is updated as Credited.


9. A pacs.002 message is passed to reverse the payment.
10. Once the pacs.002 message is processed, the new payment is created in status 4.


11. After running the BNK/PAYMENTS.STPFLOW.LIGHT service, the payment moves to status 999.


12. The original payment moves to status 998.


13. The *Status* of the DEBIN order is updated as Crediting Error.



[Incoming Recurrent DEBIN in Initiated Status](#)

When an incoming recurrent DEBIN is received, if there is an issue while processing the payment in Temenos Payments Hub and communicating it with the clearing house (COELSA response does not exist), the DEBIN status is moved to In Progress due to a validation failure (FCM hit, posting restrictions, etc.). Temenos Payments Hub sends the 30 - Otros problemas con la cuenta de Débito message to COELSA. If a positive acknowledgement (OK) response is received from COELSA, the status is moved to Debit Error. If a negative acknowledgement (NOT-OK) is received from COLESA, Temenos Payments Hub changes the status to Data Error. If there is no response received from clearing after the configured retry, the recurrent DEBIN is moved to Debit Error.

When an incoming recurrent DEBIN is received (debit account number is invalid) and while communicating it with the clearing house (COELSA response does not exist), the DEBIN status is moved to In Progress due to a validation failure (invalid account number). Temenos Payments Hub sends to COELSA the 30 - Otros problemas con la cuenta de Débito message. If a positive acknowledgement (OK) response is received from COELSA, the status is moved to Debit Error. If a negative acknowledgement (NOT-OK) is received from COLESA, Temenos Payments Hub changes the status to Data Error. If there is no response received from clearing after the configured retry, the recurrent DEBIN is moved to Debit Error.

In the following example, an incoming recurrent DEBIN is received with incorrect data in any of JSON fields and a positive acknowledgement (OK) is received from COELSA.

1. The following OFS is processed to create a DEBIN order.


2. In the OFS message above, the highlighted portion is the incorrect debit account provided.
3. The *Status* of the DEBIN order is updated as In-progress.


4. The following OFS message is processed.


5. The *Status* of the DEBIN order remains as Debit Error.



## DEBIN Request Initiation (Seller to COELSA)

1. To initiate a DEBIN request, launch the DEBIN application and go to **Debit Order request/response**>**Debit Order request/response-Outward**>**Create Debit Order**.



2. Once the seller initiates a DEBIN request, a record is created in PPADEB.DEBIT.ORDER with *Direction* as ‘Outward’. Temenos Transact validates the request and sends an IF event (which is consumed by L2 layer) to move the request to COELSA.
3. COELSA acknowledges the request with a unique 22 digit Univocal reference and provides the expiration time of the DEBIN request. The Univocal ID generated by COELSA is stored in the *Transaction* *Reference* field.

When initiating debin order payments, users can use the COELSA *Recurrence Id* instead of the Temenos Transact *Id*.

The bank user will have the COELSA *Recurrence Id* received from clearing. This value is common for both the buyer and seller.

The PPADEB.DEBIT.ORDER,INITIATION version allows users to input the COELSA *Recurrence Id* when initiating a debin order payment.

A drop down is provided in the *Recurrence Id* field, which will list of the existing *Recurrence Id* details.



When selecting the *Recurrence Id* as True, then the *Recurrence Id* field cannot be left blank, otherwise the following error will be displayed: *Recurrence Id cannot be empty when recurrence is TRUE.*

[Status Update by L2 layer](#)

On receiving the acknowledgement, the *Status* is updated as ‘Initiated’ in the PPADEB.DEBIT.ORDER application.



[Enquiry to View Outgoing Debit Orders](#)

To view all outgoing debit orders, launch the DEBIN application and go to **Debit Order Requests/Response**>**Debit Order Requests – Outward**>**View Debit Order**.



## DEBIN Request Received (COELSA to Buyer)

The buyer bank receives the DEBIN order notification (for the DEBIN request initiated by the seller) from COELSA. A record is created in the Debit Order application (PPADEB.DEBIT.ORDER) with *Direction* as ‘Inward’ and *Status* as ‘Initiated’.



[Accept or Reject Incoming Request (Buyer)](#)

A buyer can accept or reject the DEBIN request by setting the *Operation* field as Accept or Reject (In Model, an enquiry with option defaulted as Accept is provided).



Once accepted, the *Status* of the PPADEB.DEBIT.ORDER is moved to In Progress and a credit transfer is initiated in Temenos Payments Hub by using the PO application.

When the user rejects a request, a rejection reason is entered in the *Rejection* *Reason* field. The following reasons are available and attached to the *Rejection* *Reason* field by using the EB.LOOKUP application.

| *Id* (Rejection Reason Code) | Description |
| --- | --- |
| 10 | Rejection by customer |
| 11 | Reject ignoring origin of DEBIN |

[Incoming Spot DEBIN in Initiated Status (Buyer)](#)

This process is described below.

[Incoming Spot DEBIN is Rejected by the Customer (Buyer)](#)

When the incoming spot DEBIN is rejected by the customer and the COELSA response exists, the DEBIN status remains as Initiated. The acknowledgement (OK) response is received from COELSA and the status is moved to Rejection from Customer. The acknowledgement (NOT-OK) is received from COLESA and Temenos Payments Hub changes the status to Data Error.

When the incoming spot DEBIN is rejected by the customer and the COELSA response does not exist, and if there is no response received from COELSA in the stipulated or configured time, the retry will be initiated. If there is still no response, Temenos Payments Hub will move back the status to Initiated for the buyer to take action (accept or reject).

When the incoming spot DEBIN is received but the customer does not accept or reject it (Initiated > Expired), the DEBIN status is moved to Expired. This will be the only possibility of reaching this status if there is no action by the buyer over any incoming DEBIN.

[Scenario 1](#)

In the following example, the incoming spot DEBIN is rejected by the customer (buyer) and a negative acknowledgement (NOT-OK) is received from COELSA.

1. The following OFS message is processed to create a DEBIN order.


2. A DEBIN order has been created and it can be checked in the PPADEB.DEBIT.ORDER application.


3. The *Status* of the record is Initiated in the beginning.
4. After this, the DEBIN order needs to be rejected using the PPADEB.DEBIT.ORDER,ACCEPT.REJECT version.


5. The *Status* of the DEBIN order remains Initiated and the *Response Code* is updated.


6. The following OFS message is processed to update the status of the DEBIN order.


7. The *Status* is updated as Data Error.



[Scenario 2](#)

In the following example, an incoming spot DEBIN is rejected by the customer (buyer) with a validation error due to insufficient funds and a positive acknowledgement (OK) is received from COELSA.

1. The following OFS message is processed to create a DEBIN order.


2. A DEBIN order has been created and it can be checked in the PPADEB.DEBIT.ORDER application.


3. The *Status* of the record is Initiated in the beginning.
4. After this, the DEBIN order needs to be accepted using the PPADEB.DEBIT.ORDER,ACCEPT.REJECT version.


5. The *Status* is updated as In-progress.


6. Once the DEBIN order is accepted, a payment order is generated by Temenos Payments Hub and the payment is in status 4.


7. Start the BNK/PAYMENT.STPFLOW.MEDIUM service and the payment moves to status 997.


8. The *Response Code* is updated as 20 and the *Status* is In-progress.


9. The following OFS message is processed.


10. The *Status* of the DEBIN order is updated as Insufficient Funds.



[Incoming Spot DEBIN is Accepted by the Customer (Buyer)](#)

When the customer accepts the incoming spot DEBIN and the COELSA response exists, the DEBIN status moves to In Progress after the successful validation. The Confirmo debito message is sent to clearing. A positive acknowledgement (OK) is received from COLESA and the status moves to Credited. If a negative acknowledgement (NOT-OK) is received from COLESA, Temenos Payments Hub changes the status to Data Error.

When the customer accepts the incoming spot DEBIN and the COELSA response exists, but COELSA notifies about an issue while crediting the seller, the DEBIN status is moved to In Progress after the successful validation. The Confirmo debito message is sent to clearing. A positive acknowledgement (OK) is received from COLESA and the status moves to Credited. After the SLA configured by the clearing house, there is a rejection request to revert the payment. After this time, Temenos Transact moves DEBIN to the Credit Error status, the payment is reversed and the status is changed to 998.

When the customer accepts the incoming spot DEBIN and the COELSA response does not exist because of an issue while communicating with the clearing house, the DEBIN status is moved to In Progress after the successful validation. The Confirmo debito message is sent to clearing. A positive acknowledgement (OK) is received from COLESA and the status moved to Credited. If a negative acknowledgement (NOT-OK) is received from COLESA, Temenos Payments Hub changes the status to Data Error. If there is no response received from COELSA in the stipulated or configured time, the payment is moved back to the Initiated status.

When the customer accepts the incoming spot DEBIN and the COELSA response exists but there is an issue inside the Temenos Payments Hub flow, the DEBIN status moves from Initiated to In Progress due to a validation failure, other than insufficient funds. A positive acknowledgement (OK) response is received from COELSA and the status moves to Debit Error. If a negative acknowledgement (NOT-OK) is received from COLESA, Temenos Payments Hub changes the status to Data Error.

When the customer accepts the incoming spot DEBIN and if there is an issue while processing the payment in the Temenos Payments Hub and communicating with the clearing house, the DEBIN status moves to In Progress due to a validation failure other than insufficient funds. A positive acknowledgement (OK) response is received from COELSA and the status moves to Debit Error. If a negative acknowledgement (NOT-OK) is received from COLESA, Temenos Payments Hub changes the status to Data Error. If there is no response received from COELSA in the stipulated or configured time, the payment is moved back to Initiated status from In Progress.

[Scenario 1](#)

In the following example, the incoming spot DEBIN is accepted by the customer (buyer) and a positive acknowledgement (OK) is received from COELSA.

1. The following OFS message is processed to create a DEBIN order.


2. A DEBIN order has been created and it can be checked in the PPADEB.DEBIT.ORDER application.


3. The *Status* of the record is Initiated in the beginning.
4. After this, the DEBIN order needs to be accepted using the PPADEB.DEBIT.ORDER,ACCEPT.REJECT version.


5. The *Status* is updated as In-progress.


6. Once the DEBIN order is accepted, a payment order is generated by Temenos Payments Hub and the payment is in status 4.
7. Start the BNK/PAYMENT.STPFLOW.MEDIUM service and the payment moves to the status 687.


8. The following OFS message is processed.


9. The payment moves to status 999.


10. The *Status* of the DEBIN order is now updated as Credited.



[Scenario 2](#)

In the following example, an incoming spot DEBIN is accepted by the customer (buyer) with a validation error other than insufficient funds and there is no response received from COELSA.

1. The following OFS message is processed to create a DEBIN order.


2. A DEBIN order has been created and it can be checked in the PPADEB.DEBIT.ORDER application.


3. The *Status* of the record is Initiated in the beginning.
4. After this, the DEBIN order needs to be accepted using the PPADEB.DEBIT.ORDER,ACCEPT.REJECT version.


5. The *Status* is updated as In-progress.


6. Once the DEBIN order is accepted, a payment order is generated by Temenos Payments Hub and the payment is in status 4.


7. Start the BNK/PAYMENT.STPFLOW.MEDIUM service and the payment moves to status 997.


8. The *Response Code* is updated as 30 and the *Status* is In-progress.


9. The following OFS message is processed.


10. The *Status* of the DEBIN order is updated as Initiated and the DEBIN order can be accepted or rejected again.



[Incoming Spot DEBIN Collection Request to Debit Buyer (Buyer)](#)

When the incoming spot DEBIN is received with incorrect data in any of the JSON fields of /AvisoDebinPendiente (CUITs, CBUs, ALIAS) at the buyer, the DEBIN status is moved to In Progress and the proper error request is sent to COELSA (40 - Otros problemas). After the acknowledgement is received, Temenos Transact changes the status to Data Error. It is assumed that there will not be any negative acknowledgement (NACK) received from clearing. If there is no response, the retry will be done. If there is still no response, DEBIN will be moved to Data Error.

[Created Spot DEBIN Order in Initiated Status (Seller or Creditor)](#)

The customer receives an incoming payment related to the generated DEBIN but there is an internal issue raised while processing the order. While crediting the customer, if there is an issue inside the Temenos Payments Hub, the DEBIN order is updated to Credit Error. The 05 status will be sent to COLESA.

The customer receives an incoming payment related to the generated DEBIN. After the payment process is completed and the communication is sent to COELSA, a rejection request is received through /AvisoOperacionFinalizada. The DEBIN payment is moved to Credited 999 (Completed) status. If any rejection request is received between the SLA time configured by the clearing house, the payment is reverted and the DEBIN status is updated as Credit Error. The register will not be parked in any intermediate status designed by Temenos.

In the following example, an incoming spot DEBIN (seller) is received with some issue inside the Temenos Payments Hub.

1. The following OFS message is processed to create a DEBIN order.


2. A DEBIN order has been created and it can be checked in the PPADEB.DEBIN.ORDER application.


3. Initially, the DEBIN order is in Initiated status.
4. After this, a pacs.008 message is passed to initiate a payment.

   [](../../Resources/Images/Argentina/PPADBR/Debinpacs.008.xml)
5. The payment is created in status 4.


6. After running the BNK/PAYMENT.STPFLOW.LIGHT service, the payment moves to status 997.


7. The *Status* of the DEBIN order is updated as Crediting Error.



[Enquiry to View Incoming Debit Orders](#)

To view all incoming debit orders, launch the DEBIN application and go to **Debit Order Requests/Response**>**Debit Order Requests – Inward**>**View Debit Order**.



## Credit Transfer Processing at Temenos Payments Hub (Both Seller and Buyer)

When an incoming request is accepted by a buyer or auto-accepted, the *Status* of the debit order is changed to ‘Credited’. The reference of debit order is used to locate the transaction at Temenos Payments Hub.

Similarly, at the seller’s end, the transaction received from COELSA is linked to debit order using the *Sender* *Reference**Incoming* field. The payment status is changed to completed in Temenos Payments Hub.



To check for the payment status, paste the reference in *Sender* *Reference**Incoming* field.



Payment status is changed to completed.



## Pre-Authorisation DEBIN Request Received (COELSA to Buyer)

1. COELSA sends the DEBIN order with *P**reauthori**s**ation* *field* as True.
2. On receiving the order, it is processed as pre-authorised DEBIN payment.

   It does not wait for any manual acceptance from buyer. It is auto-accepted and payment is initiated automatically at Temenos Payments Hub.
3. Set the following values in the below fields:
   - *Auto* *Accept* – Yes
   - *Operation* − Null

All the other processes are same for normal DEBIN payment.



## Chargeback Request (Buyer to COELSA)

The buyer can request for a chargeback for the completed pre-authorised DEBIN payment. A chargeback request is sent to COELSA.

1. To initiate chargeback, go to **Debit Order Request – Inward**>**Initiate Chargeback**.
2. To raise the chargeback request, ensure the following:
   - The completed DEBIN order value date has not exceed 30 calendar days
   - The *Status* is set as ‘Credited’
3. To validate the date, use the *Max Date* *to be* *Reversed* field in PPADEB.DEBIT.ORDER.
4. To validate the status, use the *Debin* *Order Status* field.

   This request is sent to COELSA through L2 API.
5. On receiving a positive response, the chargeback request *Status* is changed to ‘In Progress’. This triggers the reversal of original transaction in Temenos Payments Hub.
6. Once the reversal transaction is completed by using TRIP status update, the chargeback *Status* is changed to ‘Chargebacked’.
7. On receiving the response, chargeback *Status* is changed to ‘Error’ and reversal is not initiated at Temenos Payments Hub.

An enquiry is provided for the user to pick the pre-authorised DEBIN payment to initiate the chargeback.









## Chargeback Notification (COELSA to Seller)

1. Chargeback notification from COELSA is forwarded to the seller.
2. On receiving the chargeback notification, the seller bank accepts it (which is already validated and accepted by COELSA).
3. On receiving the chargeback notification, the seller bank validates the following:
   - Chargeback request date has not exceed more than 30 calendar days
   - Original transaction is not already chargebacked
4. On validating the above conditions, *Status* is changed to ’Chargebacked’ in progress at the seller end. This initiates the reversal of original transaction at seller-side.



## Adhesion of Collecting Account

Using an internal account, the user can register a record with COELSA as collecting account. The bank user registers with CUIT and CBU and sends the request to COELSA. This request is sent through L2 API and the response is received from COELSA.



- On receiving a positive response, the *Status* of the record is changed to ‘Active’.
- On receiving a negative response, the *Status* of the record is changed to ‘Inactive’.

An enquiry is also provided to view the collecting account details and statuses.



## Seller DEBIN Order Cancellation Request

A seller can initiate cancellation for records with *Status* as ‘Initiated’ in PPADEB.DEBIT.ORDER. This is performed by setting the *Operation* field to ‘Cancel’.






Once cancelled, the system sends an IF event (which is consumed by L2 layer) to move the cancellation request to COELSA.

## Expiry Service

A new service checks for the following:

- Payment requests are initiated and awaits credit confirmation from COELSA
- Incoming notifications await for buyer’s acceptance

If the payments expire, the system updates the *Status* of corresponding Debit Order record as ’Expired’.

This service reads all the PPADEB.DEBIT.ORDER records with *Status* as ‘Initiated’ and ‘Reject Pending Confirmation’.

If *Direction* is ‘O’ (Outward), only records with *Status* as ‘Initiated’ is checked. Otherwise, both the statuses are checked by comparing the value in the *Expiry Date Time* field with current system date and time. If it exceeds, the service updates the *Status* as ‘Expired’.

## DEBIN Archival

New menu’s are introduced to view the history and archival files for DEBIN orders. This will help the user to view the files and sort the view as per the requirement.

- The **View Debit order History** menu allows users to view the list of history files for DEBIN orders.
- The **View Debit order Archived** menu allows users to view the archived debit orders.

[View History Debit Order](#)

1. Navigate to the **View In /Out Debit order - History / Archived >> View Debit order History** menu,


2. The list of history files is displayed below.


3. Click on the **View** icon to view the details of the history file.



[View Archival Debit Order](#)

1. Navigate to the **View In /Out Debit order - History / Archived >> View Debit order Archived** menu,


2. The list of archived files is displayed below.


3. Archived files will only be listed and the user won’t be able to view individual transactions. All the required menus are available in the header of the system (i.e. credit account number, debit account number, status or direction).

In this topic

- [Working with DEBIN Registration Clearing](#WorkingwithDEBINRegistrationClearing)

- [DEBIN Registration](#DEBINRegistration)
- [Recurrence Registration](#RecurrenceRegistration)
- [DEBIN Request Initiation (Seller to COELSA)](#DEBINRequestInitiationSellertoCOELSA)
- [DEBIN Request Received (COELSA to Buyer)](#DEBINRequestReceivedCOELSAtoBuyer)
- [Credit Transfer Processing at Temenos Payments Hub (Both Seller and Buyer)](#CreditTransferProcessingatTemenosPaymentsHubBothSellerandBuyer)
- [Pre-Authorisation DEBIN Request Received (COELSA to Buyer)](#PreAuthorisationDEBINRequestReceivedCOELSAtoBuyer)
- [Chargeback Request (Buyer to COELSA)](#ChargebackRequestBuyertoCOELSA)
- [Chargeback Notification (COELSA to Seller)](#ChargebackNotificationCOELSAtoSeller)
- [Adhesion of Collecting Account](#AdhesionofCollectingAccount)
- [Seller DEBIN Order Cancellation Request](#SellerDEBINOrderCancellationRequest)
- [Expiry Service](#ExpiryService)
- [DEBIN Archival](#DEBINArchival)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:51:42 PM IST
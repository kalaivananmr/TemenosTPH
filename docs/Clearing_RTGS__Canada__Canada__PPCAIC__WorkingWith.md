# Working with Interac Instant Payment via Central1

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Canada/Canada/PPCAIC/WorkingWith.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Regional Framework > Canada Model Bank > Interac Instant Payment via Central1 > Working with

- Regional Framework;)
  - Canada Model Bank;)
    - Interac Instant Payment via Central1;)
      - [Introduction](../../Canada/PPCAIC/Introduction.htm)
      - [Configuration](../../Canada/PPCAIC/Configuration.htm)
      - [Working with](../../Canada/PPCAIC/WorkingWith.htm)
      - [Tasks](../../Canada/PPCAIC/Tasks.htm)
      - [Outputs](../../Canada/PPCAIC/Outputs.htm)

Payments

# Working with Interac Instant Payment via Central1

Updated On 07 June 2023 |
 28 Min(s) read

Feedback
Summarize

The following functionalities are available for the Interac Instant Payment via Central1 module.

## Understanding Account Number Validation

Interac will send account number in the format below.

- 'aaa' is the financial institution identifier.
- 'bbbbb' is the transit number.
- 'cccccccc…' is the account number.

Hence, for account validations and posting into Temenos Transact, the Temenos Transact account number is retrieved from the Interac request.

The PPCAIC.INTERAC.ENRICH.API.ACCOUNT routine was modified to derive the Temenos Transact account number based on the format received from the Interac messages.

The routine was attached as a hook routine in the *Enrich API* field from the PP.MSGMAPPINGPARAMETER application.

From the incoming message of Interac, the routine will the value of the account number and pass the below values as the incoming argument. The value derived from point 2/3/4 is out argument. For example, 809-12345-100567890.

- First delimiter value = Financial institution identifier.
- Second delimiter value = Transit number.
- Third delimiter value = Account number.

Then, the routine will read the INTERCO.PARAMETER application and fetch the length of the account number.

- If the account number’s length is equal to the incoming account number, then:
  - The routine will read the ACCOUNT application. If it’s a valid account number, it will return the account number as the out argument. Else it will proceed with the actions below.
  - The routine will read the ALTERNATE.ACCOUNT application. If there is a record available, then it will get the corresponding Temenos Transact account number from the record and return the account number as the out argument. Else it will proceed with the actions below.
  - Return back with same number provided by Interact.
- If the account number length is not equal to the incoming account number, then:
  - The routine will get the *Company Code* and locate it in the INTERCO.PARAMETER application, to fetch the *Branch Code* and concat the branch code with the account number. With the concatenated value, it will do the below:
    - Read the ACCOUNT application and if there isn’t a valid account number, it will return the account number as the out argument. Else it will proceed as per below.
    - Read the ALTERNATE.ACCOUNT application and if there is a record available, then it will get the corresponding Temenos Transact account number from the record and return the account number as the out argument. Else it will proceed as per below.
- If the Temenos Transact account is not fetched based on the above logic, the routine will return back with same number provided by Interact.

The account number position in Temenos Payments Hub is fetched based on the party role for each message type.

| Message Type | Party Role | Position |
| --- | --- | --- |
| Pacs.008 | BENFCY | CreditPartyOrgIdOtherId |
| Pacs.003 | DEBTOR | DebitPartyOrgIdOtherId |
| Pacs.004 | BENFCY | CreditPartyAccountLine |
| Pacs.007 | BENFCY | CreditPartyAccountLine |

1. The branch code of the account is passes into the request as per the INTERCO.PARAMETER record below.


2. An incoming message is received from Interac – pacs008/003/007.
3. The message is placed in the queue defined for C1 clearing.
4. The message will have details for the roles below:
   - Direct account.
   - Alternate account.
   - Contacting *Company Id* and account.
5. As an example, the account number was placed into the *Address Line1* of the BENFCY role .
6. The file placed into Interac queue path .
7. Run the INWARD.MAPPING service and verify the POR.TRANSACTION and POR.SUPPLEMENTARY.INFO applications to validate actual Temenos Transact account number returned.

## Understanding Interac eTransfer

The Interac adapter was built to connect Central1 and Temenos Payments Hub. The Interac adapter will consume the incoming request payload from central1.

The incoming request message payload is processed through the Temenos Payments Hub request queue and the Temenos Payments Hub response queue returns back an RAW xml.

The response received from Temenos Payments Hub response queue will be in raw xml format. This will then be converted to the equivalent response payload before sending it to Central1.

Exceptions due to connectivity or invalid message format are captured in the log file configured in the property file.

[Design Time](#)

The design time process is explained below.

[Message Authentication](#)

Message authenticity is validated using the signature verification. Signature verification will happen through Hook API or Internal API. A switch will be configured in the application.properties file.

[Case 1: Authentication Failure due to JWS Token Failure](#)

1. The external.signature.verify is set as false in application.properties file as shown below.



   Valid Certificate - bhapi-sign-key-123456780013800001Rb5wmAAB001.dev.abccu.ca

   Invalid Certificate - ahapi-sign-key-123456780013800001Rb5wmAAB001.dev.abccu.ca
2. Post the message with invalid certificate.


3. A response is received with an error as 403.


4. The log file is shown below for reference. As expected, the HTTP error code 403 is returned. Also, the error information is captured in the log file.



[Case 2: Authentication Failure due to Invalid Signature](#)

1. The external.signature.verify is set as false in application.properties file as shown below.


2. A valid signature is provided below:

   ewoiYWxnIjoiUlMyNTYiLAoia2lkIjoiYmhhcGktc2lnbi1rZXktMTIzNDU2NzgtMDAxIiwKImN0eSI6ImFwcGxpY2F0aW9uL2pzb24iLAoiYjY0Ijp0cnVlLAoiY3JpdCI6WyJiNjQiXQp9.ewogICAgInBheW1lbnRPcmRlcklkIjogIlBPMTIzNDU2MTMiLAogICAgInRyYW5zYWN0aW9uRGF0ZSI6ICIyMDIwMTAwOSIsCiAgICAidHJhbnNhY3Rpb25BbW91bnQiOiAiMTAwIiwKICAgICJhZGRyZXNzRGV0YWlsIjogIjEuMjMiLAogICAgImFkZHJlc3MiOiAiY2hlbm5haSAtIDYwMDAwMSIsCiAgICAiZnJhdWRDaGVja1JlcXVpcmVkIjogIk5PIgogfQ==.lhqHiDphhzNOvMvRPUJnBffZRZRHgPw2q+5geHwUz/bnUccyIif3QBVBFiCis+80SMjOMj21OPvvIfXFul1tV4wx0Fn07Yafdhj4DY9SmUfgAt5gf+43Z50Os2g60tYFLZgeNrUeqBIjx050tMkpxW8bY9lHNi7T5mgthXZNXsfTFUmuYxVMSVgiSt7PY3PiZu7YGZmSPlAWw6CCJsSX92VOQgCpSddw7cF4xrBFWHwQgz31tztichiq3oGVt/fjNnt6mG4HqDOwNWzoNxKDrYHVNaullmmeH7uvKRcp6I8jolYRx/Yv2H3j0qAe4bcLoz4ZVlSxRBEpGgg6OgGiQw==
3. An invalid signature is provided below:

   abcYWxnIjoiUlMyNTYiLAoia2lkIjoiYmhhcGktc2lnbi1rZXktMTIzNDU2NzgtMDAxIiwKImN0eSI6ImFwcGxpY2F0aW9uL2pzb24iLAoiYjY0Ijp0cnVlLAoiY3JpdCI6WyJiNjQiXQp9.ewogICAgInBheW1lbnRPcmRlcklkIjogIlBPMTIzNDU2MTMiLAogICAgInRyYW5zYWN0aW9uRGF0ZSI6ICIyMDIwMTAwOSIsCiAgICAidHJhbnNhY3Rpb25BbW91bnQiOiAiMTAwIiwKICAgICJhZGRyZXNzRGV0YWlsIjogIjEuMjMiLAogICAgImFkZHJlc3MiOiAiY2hlbm5haSAtIDYwMDAwMSIsCiAgICAiZnJhdWRDaGVja1JlcXVpcmVkIjogIk5PIgogfQ==.lhqHiDphhzNOvMvRPUJnBffZRZRHgPw2q+5geHwUz/bnUccyIif3QBVBFiCis+80SMjOMj21OPvvIfXFul1tV4wx0Fn07Yafdhj4DY9SmUfgAt5gf+43Z50Os2g60tYFLZgeNrUeqBIjx050tMkpxW8bY9lHNi7T5mgthXZNXsfTFUmuYxVMSVgiSt7PY3PiZu7YGZmSPlAWw6CCJsSX92VOQgCpSddw7cF4xrBFWHwQgz31tztichiq3oGVt/fjNnt6mG4HqDOwNWzoNxKDrYHVNaullmmeH7uvKRcp6I8jolYRx/Yv2H3j0qAe4bcLoz4ZVlSxRBEpGgg6OgGiQw==
4. Post a message with an invalid signature.


5. A response is received with an error code as 403.


6. The log file is displayed below for reference, and the error details are updated as shown below.



[Message Conversion](#)

The incoming ISO20022 JSON message is converted to Temenos Payments Hub neutral format (XML format) with apache XJ component. The converted message is then posted into the Temenos Payments Hub queue configured in the property file.

The outgoing XML message is converted back to ISO20022 JSON message (PACS.002) using the apache XJ component.

1. Post a credit pacs.008 Json message into Temenos Payments Hub.


2. The message is posted.


3. The INTERACREQ queue is refreshed with the message in neutral format.


4. The above XML message is processed in TPH and the response is updated as shown below.


5. The response message for Pacs 008 in XML is displayed below.


6. The above XML is converted back to Json format.

    [](../../Resources/Images/Canada/PPCAIC/pacs.008_Response.txt)

[Error Logging](#)

Any exception which occurs during the request processing like signature validation, timeout exception will be logged inside the package in the Log folder as shown below.



All these exceptions can also be captured separately by configuring the error.log.path property in the application.properties file. A sample is provided below.



[Case 1: Invalid Signature](#)

1. The external.signature.verify is set as false in the application.properties as shown below.


2. A valid signature is provided below:

   ewoiYWxnIjoiUlMyNTYiLAoia2lkIjoiYmhhcGktc2lnbi1rZXktMTIzNDU2NzgtMDAxIiwKImN0eSI6ImFwcGxpY2F0aW9uL2pzb24iLAoiYjY0Ijp0cnVlLAoiY3JpdCI6WyJiNjQiXQp9.ewogICAgInBheW1lbnRPcmRlcklkIjogIlBPMTIzNDU2MTMiLAogICAgInRyYW5zYWN0aW9uRGF0ZSI6ICIyMDIwMTAwOSIsCiAgICAidHJhbnNhY3Rpb25BbW91bnQiOiAiMTAwIiwKICAgICJhZGRyZXNzRGV0YWlsIjogIjEuMjMiLAogICAgImFkZHJlc3MiOiAiY2hlbm5haSAtIDYwMDAwMSIsCiAgICAiZnJhdWRDaGVja1JlcXVpcmVkIjogIk5PIgogfQ==.lhqHiDphhzNOvMvRPUJnBffZRZRHgPw2q+5geHwUz/bnUccyIif3QBVBFiCis+80SMjOMj21OPvvIfXFul1tV4wx0Fn07Yafdhj4DY9SmUfgAt5gf+43Z50Os2g60tYFLZgeNrUeqBIjx050tMkpxW8bY9lHNi7T5mgthXZNXsfTFUmuYxVMSVgiSt7PY3PiZu7YGZmSPlAWw6CCJsSX92VOQgCpSddw7cF4xrBFWHwQgz31tztichiq3oGVt/fjNnt6mG4HqDOwNWzoNxKDrYHVNaullmmeH7uvKRcp6I8jolYRx/Yv2H3j0qAe4bcLoz4ZVlSxRBEpGgg6OgGiQw==
3. An invalid signature is provided below:

   abcYWxnIjoiUlMyNTYiLAoia2lkIjoiYmhhcGktc2lnbi1rZXktMTIzNDU2NzgtMDAxIiwKImN0eSI6ImFwcGxpY2F0aW9uL2pzb24iLAoiYjY0Ijp0cnVlLAoiY3JpdCI6WyJiNjQiXQp9.ewogICAgInBheW1lbnRPcmRlcklkIjogIlBPMTIzNDU2MTMiLAogICAgInRyYW5zYWN0aW9uRGF0ZSI6ICIyMDIwMTAwOSIsCiAgICAidHJhbnNhY3Rpb25BbW91bnQiOiAiMTAwIiwKICAgICJhZGRyZXNzRGV0YWlsIjogIjEuMjMiLAogICAgImFkZHJlc3MiOiAiY2hlbm5haSAtIDYwMDAwMSIsCiAgICAiZnJhdWRDaGVja1JlcXVpcmVkIjogIk5PIgogfQ==.lhqHiDphhzNOvMvRPUJnBffZRZRHgPw2q+5geHwUz/bnUccyIif3QBVBFiCis+80SMjOMj21OPvvIfXFul1tV4wx0Fn07Yafdhj4DY9SmUfgAt5gf+43Z50Os2g60tYFLZgeNrUeqBIjx050tMkpxW8bY9lHNi7T5mgthXZNXsfTFUmuYxVMSVgiSt7PY3PiZu7YGZmSPlAWw6CCJsSX92VOQgCpSddw7cF4xrBFWHwQgz31tztichiq3oGVt/fjNnt6mG4HqDOwNWzoNxKDrYHVNaullmmeH7uvKRcp6I8jolYRx/Yv2H3j0qAe4bcLoz4ZVlSxRBEpGgg6OgGiQw==
4. Post a message with an invalid signature.


5. A response is received with the error code as 403.


6. The log file is shown for reference, and the error details are updated as shown below.



[Case 2: Invalid Message Structure](#)

1. A Pacs008 with an invalid message format is provided below (the message identification is not closed with ,).

   [ ](../../Resources/Images/Canada/PPCAIC/pacs008.Invalid msg.txt)
2. Post the above Pacs008 message.


3. An error is generated as per below.


4. View the error description.



[Heart Beat](#)

The heartbeat enables monitoring or checking that the bank host system is up and not offline.

Central 1 sends heartbeat requests to the bank host and expects the bank host to reply with the current status of the Temenos Transact within 1.5 sec (whether active or not).

1. A sample of a heart beat URL with HTTP is highlighted below.


2. Post the heartbeat message.


3. The response is 200, as Temenos Transact is up and active.


4. If Temenos Transact is down and not active, the status code 404 is sent, as shown below.


5. The error log is updated for the heart beat failure, as shown below.



## Understanding Interac Instant Payment Clearing

The Interac instant message types in scope are provided below:

| Message from C1 to Temenos Payments Hub | ISO 20022(JSON) |
| --- | --- |
| Inward debit request | Pacs.003 |
| Initiate deposit (credit) of funds to account | Pacs.008 |
| Reverse (undo) previous withdrawal (debit) instruction | Pacs.007 |
| Return | Pacs.004 |
| Debit or credit posting request response ( for Pacs.003,Pacs.004 & Pacs.008) | Pacs.002 |



| Message from Temenos Payments Hub to C1 | ISO 20022(JSON) |
| --- | --- |
| Account validation response including charges(If any) for inward credit or debit request or return request - (success or failure) | Pacs.002 |
| Credit or debit posting (success) response in customer account | Pacs.002 |
| Credit or debit posting (failure) response in customer account | Pacs.002 |

ISO20022 messages are API based JSON messages, hence the system is able to interface with C1 to accept the ISO20022 JSON messages.

Interac messages flow is a two steps process:

1. Proposal: The system will validate if the account number is correct, if there are any restrictions or charges associated with the transaction and responds with success or failure along with the charge details. In case funds are reserved during the proposal and there is no posting request, then the reservation will be cancelled and all transaction will be reversed using the default time out setting.
2. Posting: If the customer accepts the request, C1 will send the debit or credit request to Temenos Payments Hub. In case of any issues during posting, the reservation and transaction will be reversed. Any failure on posting will reverse the reservation or transaction posted.

In case of a reversal, the charges debited in the customer account will be reversed.

[Process Pacs.003 Incoming Direct Debit Requests](#)

When a customer initiates a payment from an online channel, the request will be sent to C1.

C1 will send a pacs.003 proposal message to the debtor bank to debit the customer’s account.

The payments hub system will check if there is any duplicate payment received and will send a negative confirmation to C1 in case there is a duplicate.

Once the pacs.003 is received, account validations, funds reservation and charge calculation check will be performed by Temenos Transact. The account validation response along with the charge information will then be sent to the payments hub.

In case of successful account validation, a positive account validation response is sent to C1 along with the charge information. The incoming pacs.003 request will be parked in the awaiting confirmation status.

In case of account validation failure then a negative response is sent to C1 with the appropriate error code in the pacs.002 message. The incoming pacs.003 request will be marked as cancelled in the payments hub.

The system will check the maximum instant payment time out to respond to the incoming pacs.003. If it has breached the SLA, the payments hub will send a negative confirmation to C1.

C1 responds with a debit confirmation request for the positive account validation response.

The payments hub processes the pacs.002 debit confirmation request from C1 and does the posting to debit the customer account.

In case of any positing failure, the payments hub will send a negative acknowledgment (pacs.002) message to C1 with the appropriate error code. The incoming pacs.003 payment will be marked as cancelled in the payments hub and the funds reservation will be cancelled along with the charges amount.

If the posting is successful then payments hub will send a positive acknowledgement message (pacs.002) to C1.

If the debit confirmation request is not received from C1 after a certain time period (time out period configured in the payments hub), the payments hub will select all the payments awaiting confirmation from C1 which have timed out and cancel all such payments.

The workflow is provided below:



1. View the transaction details using the ENQ PAY.PEN.PROCESS enquiry.


2. Check the details of the transaction using the IF.EVENTS.INTERFACE.TABLE application as per below.


3. The transaction is created in the POR.SUPPLEMENTARY.INFO application as per below.


4. Check the transaction details in the Repair DD View Screen as per below.


5. Check the Audit trail to view the transaction details.



[Process Inward Pacs.008 Credit Requests](#)

An incoming pacs.008 from central 1 will be received by the payment hub and the payments hub system will check if there is any duplicate payment received and will send a negative confirmation to C1.

Once the pacs.008 is processed, account validations (posting restrictions, account closed) check will be performed by the Temenos Transact system and the account validation response is sent to the payments hub.

In case of successful account validation, a positive account validation response is sent to C1. The incoming pacs.008 request will be parked in a status awaiting confirmation.

In case of account validation failure then a negative response is sent to C1 with an appropriate error code in the pacs.002 message. The incoming pacs.008 request will be marked as cancelled in the payments hub.

The system will check the maximum instant payment time out to respond to the incoming pacs.008. If it has breached the SLA, the payments hub will send a negative confirmation to C1.

In case an account validation response (pacs.002) is sent to C1 and does not reach the C1 system within the SLA due to technical issues, C1 will not send any response back to the bank host. The payments hub will select all the payments awaiting confirmation which have timed out (time out period configured in payments hub) and cancel all such payments .

C1 will respond with a credit confirmation request for the positive account validation response.

The payments hub will then process the pacs.002 credit confirmation request from C1 and perform the posting to credit the customer account.

In case of any positing failure, the payments hub will send a negative acknowledgment (pacs.002) message to C1 with an appropriate error code. The incoming pacs.008 payment will be marked as cancelled in the payments hub.

If the posting is successful then the payments hub will send a positive acknowledgement message (pacs.002) to C1.

The workflow is provided below:



1. View the transaction details using the ENQ PAY.PEN.PROCESS enquiry.


2. The transaction is created in the POR.SUPPLEMENTARY.INFO application as per below.


3. Check the Audit trail to view the transaction details.



[Process Pacs.004 Incoming Return Requests from C1](#)

Incoming pacs.004 from central 1 will be received by payment hub and the payments hub system will check for any duplicate payment received and send a negative confirmation to C1.

Once the pacs.004 is processed, account validations (posting restrictions, account closed) check will be performed by the Temenos Transact system and the account validation response is sent to the payments hub.

In case of successful account validation, a positive account validation response is sent to C1 and the incoming pacs.004 request will be parked in awaiting confirmation status.

In case of account validation failure then a negative response is sent to C1 with an appropriate error code in the pacs.002 message. The incoming pacs.004 request will be marked as cancelled in the payments hub.

When the account validation response (pacs.002) message is not received by C1 within the SLA, C1 will initiate new pacs.004 for the same pacs.003 again, the system will check if the pacs.004 is received for the first time for the underlying pacs.003 by checking the return received indicator in the payment hub.

If the return received indicator is not set to Y, then a new return transaction will be processed as explained above.

If the returned is already set to Y, then a new return transaction will not be created and a pacs.002 confirmation message will be sent again based on the status of the pacs.004 received for the first time. In this case, the subsequent pacs.004 will be received with new unique reference (new message id).

C1 will then respond with a return credit confirmation request for the positive account validation response.

The payments hub will process the pacs.002 return credit confirmation request from C1 and perform the posting to credit the customer account.

In case of any positing failure, the payments hub will send a negative acknowledgment (pacs.002) message to C1 with an appropriate error code. The incoming pacs.004 payment will be marked as cancelled in the payments hub.

If the posting is successful then the payments hub will send a positive acknowledgement message (pacs.002) to C1.

The charges amount debited in the incoming pacs.003 will not be reversed along with the incoming pacs.004.

If the credit confirmation request is not received from C1 after certain time period (time out period configured in the payments hub), the payments hub will select all the payments awaiting confirmation from C1 which have timed out and cancel all such payments.

The workflow is provided below:



1. View the transaction details using the ENQ PAY.PEN.PROCESS enquiry.


2. The original payment is displayed below.


3. The return payment is displayed below.



[Process Inward Pacs.007 Reversal Request from C1](#)

A pacs.007 reversal request can be received in the following cases.

- Pacs.007 for a pacs.008/pacs.003/pacs.004 is received when the pacs.002 message sent after doing the account posting to C1 is failed due to SLA breach, in such scenario, C1 will send the pacs.007 reversal request to reverse the debit or credit posting.
- Pacs.007 for a pacs.003 can be received when C1 is unable to transmit the pacs.008 to the creditor bank due to technical issue, in such a scenario, C1 will send the pacs.007 reversal request to the debtor bank to reverse the debit posting.

An incoming pacs.007 from central 1 will be received by payment hub and the payments hub system will check for any duplicate payment received and send a negative confirmation to C1.

Once the pacs.007 is processed, account validations (posting restrictions, account closed) check will be performed by the Temenos Transact system and the reversal posting is done to the credit the customer account. The reversal posting response is sent to the payments hub.

In case of successful posting, a positive account validation response is sent to C1.The status of the incoming pacs.007 will be marked as completed and the status of the pacs.003/pacs.008/pacs.004 message will be marked as reversed.

The charge amount debited in the incoming pacs.003 will be reversed and credited back to customer account, along with the reversed transaction amount.

In case of account validation failure, a negative response is sent to C1 with an appropriate error code in the pacs.002 message. The incoming pacs.007 request will be marked as rejected in the payments hub.

While processing the incoming pacs.007, if the underlying pacs.008, pacs.003 or pacs.004 is not in completed status and is in rejected or cancelled status, the reversal posting will not be done and a negative pacs.002 confirmation will be sent to C1. The reject reason code in the pacs.002 will be same as the reason code sent in the debit or credit confirmation response sent to C1 previously for a pacs.008, pacs.003 or pacs.004. The status of the pacs.007 will be marked as rejected.

While processing the incoming pacs.007, if the underlying pacs.008, pacs.003 or pacs.004 is not in completed status and is in-progress status then the pacs.007 will be rejected by sending a pacs.002 RJCT with 999 as the reason code. The status of the pacs.007 will be marked as rejected.

When the account validation response (pacs.002) message is not received by C1 within the SLA, C1 will initiate new pacs.007 for the same pacs.003, pacs.008 or pacs.004 again. The system will check if the pacs.007 is received for the first time for the underlying pacs.003, pacs.008 or pacs.004 by checking the reversal indicator in the payment hub.

If the reversal indicator is not set to Y, then a new reversal transaction will be processed as explained above.

If the reversal is already set to Y, then a new reversal transaction will not be created and a pacs.002 confirmation message will be sent again based on the status of the pacs.007 received for the first time.

The workflow is provided below:



[Payments SLA for Different Message Types](#)

The SLA is determined from the PP.CHANNEL.CUTOFF application (message type EQ pacs.003), based on the clearing nature code of the underlying pacs.003.

The incoming pacs.003 or pacs.008 with local instrument proprietary tag with the following values is treated as an INST payment:

- REALTIME\_ACCOUNT\_ALIAS\_PAYMENT.
- REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT.

The incoming pacs.003 or pacs.008 with local instrument proprietary tag with the following values is treated as a NRINST payment:

- REGULAR\_PAYMENT.
- FULFILL\_REQUEST\_FOR\_PAYMENT.
- ACCOUNT\_ALIAS\_PAYMENT.
- ACCOUNT\_DEPOSIT\_PAYMENT.

The SLA details are provided below, for each pacs type:

| PACS Type | Instrument Type | SLA | Remarks |
| --- | --- | --- | --- |
| PACS008 | REALTIME\_ACCOUNT\_ALIAS\_PAYMENT  OR  REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT | 1.5 | BH should response back to PACS008 with PACS002 within 1.5 if the instrument type is  REALTIME\_ACCOUNT\_ALIAS\_PAYMENT  OR  REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT |
| PACS008 | REST - All instrument tag APART from  REALTIME\_ACCOUNT\_ALIAS\_PAYMENT  OR  REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT) | 8 Secs | BH should response back to PACS008 with PACS002 within 8s if the instrument type is NOT EQUAL TO  REALTIME\_ACCOUNT\_ALIAS\_PAYMENT  OR  REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT |
| PACS003 | REALTIME\_ACCOUNT\_ALIAS\_PAYMENT  OR  REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT | 4 Secs | BH should response back to PACS003 with PACS002 within 5s if the instrument type is  REALTIME\_ACCOUNT\_ALIAS\_PAYMENT  OR  REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT |
| PACS003 | REST - All instrument tag APART from  REALTIME\_ACCOUNT\_ALIAS\_PAYMENT  OR  REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT) | 8 Secs | BH should response back to PACS003 with PACS002 within 8s if the instrument type is NOT EQUAL TO  REALTIME\_ACCOUNT\_ALIAS\_PAYMENT  OR  REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT |
| PACS002  (Confirmation or Posting) | REALTIME\_ACCOUNT\_ALIAS\_PAYMENT  OR  REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT | 4  Secs | BH should response back to PACS003 with PACS002 within 4s if the instrument type is  REALTIME\_ACCOUNT\_ALIAS\_PAYMENT  OR  REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT |
| PACS002  (Confirmation or Posting) | REST - All instrument tag APART from  REALTIME\_ACCOUNT\_ALIAS\_PAYMENT  OR  REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT) | 8 Secs | BH should response back to PACS008 with PACS002 within 8s if the instrument type is NOT EQUAL TO  REALTIME\_ACCOUNT\_ALIAS\_PAYMENT  OR  REALTIME\_ACCOUNT\_DEPOSIT\_PAYMENT |
| PACS007 | ALL | 8 secs | Reversal Messages by default have 8 secs SLA |
| PACS004 | ALL | 8 Secs | Reversal Messages by default have 8 secs SLA |

1. View the transaction details using the ENQ PAY.PEN.PROCESS enquiry.


2. The BNK/PPCAIC.CANCEL.TIMEOUT.PAYMENTS job is created in the BATCH application as per below.


3. The transaction is created in the POR.SUPPLEMENTARY.INFO application as per below.


4. View the transaction’s status using the ENQ PAY.PEN.PROCESS enquiry.


5. The credit confirmation is not received from clearing in the defined 10 min SLA, hence the payment is cancelled.



[Rejection Reason Codes as part of Pacs.002 Message to Clearing (C1)](#)

The rejection reason codes that were configured in the payments hub are provided below.

Based on the validation response received, an appropriate reason code will be mapped to the Temenos Payments Hub error code received and the below rejection reason code will be sent in the pacs.002 sent to clearing.

| Banking host provides ISO 20022 response code to Central 1 | Error Description |
| --- | --- |
| 22 | Account does not exist |
| 24 | Account not active |
| 29 | Account is frozen / unavailable |
| 39 | Account / Currency Mismatch |
| 47 | Duplicate transaction, transaction indicated by  MsgId was already processed |
| 49 | Account Closed |
| 999 | Unspecified Application  Error |
| 40 | Initiate Transaction Not Found |
| 26 | Account cannot accept  direct deposits |
| 35 | Direct Deposit not  supported for this customer |
| 50 | Insufficient Funds |
| 46 | Fraud Risk Exceeded |
| 48 | Compliance Risk Exceeded |
| 51 | Amount Exceeds Limit |

[Duplicate Check for Rejected or Cancelled Transactions](#)

If a pacs.008, pacs.003, pacs.004 or pacs.007 is received with the same unique reference and if it matches the existing payment already received in Temenos Payments Hub and the underlying payment status is in rejected, cancelled, reversed or awaiting confirmation and it is not in completed status, then the system will not perform the duplicate check and the payment processing will be allowed.

A duplicate check will be done only if the underlying payments (pacs.003, pacs.004, pacs.007 or pacs.008) is in completed status and the duplicate payment will be rejected by sending a pacs.002 with an appropriate reason code.

For pacs.007 there is no awaiting confirmation status. Once the pacs.007 is received, it will be posted and a positive or negative confirmation will be sent.

[Send a Repost Pacs.002 Message](#)

When the credit or debit posting confirmation is received from clearing, Temenos Payments Hub will do the posting and send the account posting acknowledgement pacs.002 message to clearing.

If the account posting acknowledgement pacs.002 message is not sent to clearing within the SLA provided, then clearing will send a pacs.007 reversal request to reverse the debit or credit posting of pacs.008, pacs.003 or pacs.004. After the reversal posting, a pacs.002 acknowledgement message will be sent.

Based on the reversal posting pacs.002 acknowledgement message, clearing will send a repost pacs.002 message for the pacs.008, pacs.003 or pacs.004 to repost the original pacs.003, pacs.008 or pacs.004 again.

When the repost pacs.002 message is received, during the message mapping stage, an enrich API will to be attached to change the status of the underlying pacs.008, pacs.003 or pacs.004 status to awaiting confirmation status from the reversed status. This will be done only if the pacs.008, pacs.003 or pacs.004 is in reversed status due to pacs.007.

After the status is changed to awaiting confirmation, the pacs.002 repost message will be processed as a posting confirmation pacs.002 message request from clearing. Posting will be done to credit or debit the customer. The status of pacs.008, pacs.003 or pacs.004 will again be updated to 999 and a pacs.002 positive or negative acknowledgment will be sent to clearing based on the posting outcome.

If the repost pacs.002 message is received again for the same pacs.008, pacs.003 or pacs.004 and if the status of pacs.008, pacs.003 or pacs.004 is in 999 then, a positive pacs.002 acknowledgment response is sent to clearing. No accounting will be done.

If the repost pacs.002 message is received again for the same pacs.008, pacs.003 or pacs.004 and if the status of the pacs.008, pacs.003 or pacs.004 is rejected or cancelled, then a negative pacs.002 acknowledgment response is sent to clearing. No accounting will be done.

In this topic

- [Working with Interac Instant Payment via Central1](#WorkingwithInteracInstantPaymentviaCentral1)

- [Understanding Account Number Validation](#UnderstandingAccountNumberValidation)
- [Understanding Interac eTransfer](#UnderstandingInteraceTransfer)
- [Understanding Interac Instant Payment Clearing](#UnderstandingInteracInstantPaymentClearing)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:00:28 PM IST
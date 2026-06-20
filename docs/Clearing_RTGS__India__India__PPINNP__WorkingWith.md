# Working with NEFT Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/India/India/PPINNP/WorkingWith.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Regional Framework > India Model Bank > NEFT Clearing > Working with

- Regional Framework;)
  - India Model Bank;)
    - NEFT Clearing;)
      - [Introduction](../../India/PPINNP/Introduction.htm)
      - [Configuration](../../India/PPINNP/Configuration.htm)
      - [Working with](../../India/PPINNP/WorkingWith.htm)
      - [Tasks](../../India/PPINNP/Tasks.htm)
      - [Outputs](../../India/PPINNP/Outputs.htm)
    - RTGS Clearing;)

Payments

# Working with NEFT Clearing

Updated On 08 November 2022 |
 83 Min(s) read

Feedback
Summarize

Branch or department users as well as customers can initiate fund transfers to other financial institutions through NEFT via digital channels (internet banking, mobile banking, other channels etc.).

Outward transactions generated will reach the beneficiary via NEFT and in case of any issues the payment will be returned by the beneficiary.

## Assumptions and Exclusions

The following assumptions and exclusions are in place for this functionality.

[Assumptions](#)

N04 for a particular batch will only be received after the reception of all the N03 reject messages in the particular batch.

The F acknowledgment messages will be received in any one of the below order:

- F27->F20->F23.
- F27.
- F27->F25.

[Exclusions](#)

The mapping of pain.001, bulk file upload, salary payment, batch booking are not in scope of this document.

The advice related to N10 will be handled separately.

For the core solution to work, a bank has to move the N04 and 972 reports to the folder configured in the EB.FILE.UPLOAD.TYPE/EB.FILE.UPLOAD.PARAM application.

## Initiate Outgoing Customer Transfers

A bank user will initiate an outgoing NEFT N06 payment using the PAYMENT.ORDER,INDIA.NEFT version by inputting the following details:

- Amount.
- Debit account.
- Charge account.
- Value date.
- Execution date.
- IFSC and beneficiary name and address.
- Account type of beneficiary.
- Charges detail (charge amount, currency, waive charges fields).
- Sender to receiver information.
- LEI information (sender and receiver lei fields).
- Currency (drop down with value = INR).

The *Sender Acc Type* and *Beneficiary Acc Type* local fields have been added to the PAYMENT.ORDER,INDIA.NEFT version.

TPH will perform all core validations and process the payment in non-STP manner and move the payment to the PP.ORDER.ENTRY,REPAIR.INDIA.NEFT repair queue for the user to take action.

For processing the payment as non-STP mode, the bank has to configure the *Non-STP Indicator* field as Y in the product determination (medium weight) application.

On validation, the system will check whether the LEI details captured for the payments is greater than 50Cr. If there are any LEI validation failure, the system will display an error message and the maker can cancel the transaction at this stage or accept the override and continue the processing and payment will move to checker queue for authorisation.

A validation API has been provided in the Payment Order product to validate the threshold limit. A new threshold limit parameter application needs to be configured to check the threshold limit for LEI validation. If the user enters an amount greater than the amount configured in the threshold limit parameter application and submits or validates the payment, TPH will check if the *Receiver LEI* field has a value. If a value is not present, the following error message will be displayed: *Sender Or Receiver LEI information is missing.*

In the POA version, the *Sender LEI* will be defaulted with the *Customer Legal Id* field from the CUSTOMER application if the user enters an amount greater than the amount configured in threshold limit parameter application.

For LEI validation in TPH for payment initiated via a channel (fir example, pain.001), the system will move the payment to the repair queue if the user has entered an amount greater than the amount configured in the LEI parameter application and there is no value present in the *Receiver LEI* field. Also, the payment will be moved to the repair queue in case of the combination of the below scenario:

- The payment amount is greater than the amount configured in the LEI parameter application.
- If there is no value in the *Customer Legal Id* field of the CUSTOMER application for the particular customer.

An API is used to generate the UTR to be populated in the outward messages. The *Message User Reference* and *Bulk Senders Reference* fields in the POR transaction will be populated with the same UTR. This value will be mapped in the *Transaction Reference Number* field of the outward message in both the header and the transaction.

If the accounting is successful, the system will generate the N06 (outward payment message). Once the payment is generated, the status will be updated to 687.

The following core accounting entries will be done by the system for individual payments:

- DR. Customer account.
- CR. Nostro account.

The following will be the accounting entries for batch booking:

- DR. Customer account.
- CR. Batch suspense account.
- DR. Batch suspense account (individual payment instruction amount).
- CR. Nostro account (individual payment instruction amount).

## Settlement Acknowledgment Messages

For every N06, N07 and N10 sent, the system will receive either a positive or negative response.

The system will mark the payment as complete only after receiving all the positive responses. If the response received is negative, the system will automatically reverse the postings.

The below accounting entries will be posted for both individual payments and batch payments:

- DR. Nostro Account.
- CR. Customer Account.

[Receive an Acknowledgment Message for Outward N06 Payments](#)

1. Initiate an outward N06 payment through PO.


2. Commit the record and then authorise it with another user.


3. The payment will be created in status 4.


4. On running the the BNK/PAYMENT.STPFLOW.MEDIUM service, the payment status will move to the 235 status.


5. View the repair queue.


6. The audit trail is provided below.


7. Commit the payment from the repair queue.


8. The payment status will be moved to 315 status.


9. Authorise it. The payment moves to the 600 status.


10. On running the medium service, the status will move to 687.


11. The accounting entries are generated as per below.


12. The events get generated as per below.


13. The outward file is generated as per below.



    [](../../Resources/Images/India/PPINNP/SOGEN21105000039.txt)
14. The audit trail is provided below.



    [](../../Resources/Images/India/PPINNP/POR.SUPPLEMENTARY.INFO.pdf)

    [](../../Resources/Images/India/PPINNP/POR.TRANSACTION.pdf)

    [](../../Resources/Images/India/PPINNP/POR.POSTING.AND.CONFIRMATION.pdf)
15. TPH receives an Ack messages in the order mentioned below.
16. Process the F27 - Bank API Response Message (Tag 5 contains “PBAPI”).


17. Process the F27 - Bank API Response Message (Tag 5 contains “PBAPI”).
18. TPH receives the file and maps it.

    [](../../Resources/Images/India/PPINNP/F27-017.txt)


19. The F27 Ack message is successfully processed and the audit trail is updated as per below.


20. The PSM.BLOB application gets updated as per below.


21. Process an F20 – Acknowledgment message.
22. TPH receives the F20 message and maps it.

    [](../../Resources/Images/India/PPINNP/F20-015.txt)


23. The F20 Ack message is successfully processed and the audit trail is updated as per below.


24. The PSM.BLOB application gets updated as per below.


25. Process an F23 - delivery notification message.
26. TPH receives the F23 message and maps.

    [](../../Resources/Images/India/PPINNP/F23-015.txt)


27. The F23 Ack message is successfully processed and the audit trail is updated as per below.


28. The payment status is marked as completed - 999 status.


29. The PSM.BLOB application gets updated as per below.


30. Below screenshots pertain to a N06 payment for which negative F27 response is received.
31. Process an outward N06 payment to the 687 status.


32. The audit trail is provided below.


33. Process the F27 - Bank API Response Message (Tag 5 contains “FBAPI”).

    [](../../Resources/Images/India/PPINNP/F27-NEGATIVE-004.txt)
34. The message is received and mapped.


35. The F27 Ack message is successfully processed and the audit trail is updated.


36. The PSM.BLOB application is updated as per below.


37. A new settlement transaction gets created in status 4.


38. Run the BNK/PAYMENT.STPFLOW.LIGHT service. The settlement transaction moves to 999 status and the original payment moves to 998 status. TPH will reverse the accounting entries and move the payment to the reject status.


39. The original payment details are provided below.


40. The return payment details are provided below.


41. The following accounting entries will be posted:
    - DR. Nostro Account.
    - CR. Customer Account.


42. TPH receives a NACK with F27 (Tag 5 contains “PBAPI”).
43. The NEFT payment is initiated with intermediary status ( 687 status).


44. The audit trail is provided below.


45. The F27 Ack message is successfully processed and the audit trail is updated as per below.

    [](../../Resources/Images/India/PPINNP/F27-018.txt)


46. The PSM.BLOB application is updated as per below.


47. TPH receives a NACK with F25 - negative acknowledgment F27 (PBAPI).

    [](../../Resources/Images/India/PPINNP/F25-012.txt)


48. The NACK F25 is successfully processed and the audit trail is updated as per below.


49. The PSM.BLOB application is updated as per below.


50. New settlement transaction gets created at status 4. After running the BNK/PAYMENT.STPFLOW.LIGHT service, the settlement transaction moves to the 999 status and the original payment moves to the 998 status.


51. The original transaction is provided below.


52. The return transaction is provided below.


53. The following accounting entries will be posted:
    - DR. Nostro Account.
    - CR. Customer Account.



## N03 Message from Clearing for Outward Payments

For the outgoing payments, clearing can send reject payments as N03 (single/bulk). When receiving the N03 message, the original transaction will be reversed and a new settlement transaction will be created and updated to the completed status.

The following accounting entries will be posted for both individual payments and batch payments:

- DR. Nostro Account.
- CR. Customer Account.

If the reject code of the N03 message is equal to any of the below reason code, TPH will treat N03 as a reschedule message and no action will be taken:

- 094 – Batch does not exist on Saturday.
- 098 – Holiday at RBI.
- 099 – Past Value Date.
- 100 – Late Arrival for a batch.

[Process an Incoming Reject N03 for Individual Outward N06](#)

1. Process an outward N06 till the 999 status.


2. Process an inward N03 message for the above payment.



   [](../../Resources/Images/India/PPINNP/Files/N03SINGLE001.txt)
3. The message gets mapped.


4. A reject transaction gets created for the original payment.


5. The audit trail for the original payment is updated as per below.


6. The `PSM.BLOB` application is updated as per below.


7. Run the BNK/PAYMENT.STPFLOW.LIGHT service and the reject transaction moves to the 999 status and the original payment moves to the 998 status.


8. The audit trail for the rejected transaction is updated as per below.


9. The accounting entries are updated as per below.


10. The posting lines are updated as per below.


11. The `POR.TRANSACTION` application is updated as per below.



[Process an Incoming Reschedule N03 for Individual Outward N06](#)

1. Process an outward N06 till the 999 status.


2. Process an inward reschedule N03 message for the above payment.



   [](../../Resources/Images/India/PPINNP/Files/N03SINGLE003.txt)
3. The message gets mapped but no reject transaction gets created because the reject code of the N03 message is 094 – Batch does not exist on Saturday. TPH will treat the N03 as a reschedule message and no action will be taken.


4. The audit trail of the original payment is provided below.


5. The `PSM.BLOB` application is provided below.



[Process an Incoming Bulk Reschedule N03 for an Outward N06](#)

1. Process an outward N06 until it reaches the 999 status.
2. The details of the first payment are provided below.


3. The details of the second payment are provided below.


4. Process an inward bulk reschedule N03 message for the above payments.

   [](../../Resources/Images/India/PPINNP/Files/N03-BULK-032.txt)



   094 is the reschedule reason code.
5. The message gets mapped but no reject transaction gets created. There is no change to the status code of the original payment, no update to the audit trail and to the `PSM.BLOB` application as well.


6. There is no change to the status code of the original payment.
7. The details of the first payment are provided below.


8. The details of the second payment are provided below.


9. The audit trail for the first payment doesn’t get updated.


10. The audit trail for the second payment doesn’t get updated.


11. There is no change to the `PSM.BLOB` application for the first payment.


12. There is no change to the `PSM.BLOB` application for the second payment.



[Process an Incoming Bulk Reject, Reschedule N03 for an Outward N06](#)

1. Process an outward N06 until it reaches the 999 status.
2. The details of the first payment are provided below.


3. The details of the second payment are provided below.


4. Process an inward bulk N03 message for the above payments.

   [](../../Resources/Images/India/PPINNP/Files/N03-BULK-033.txt)



   094 is the reschedule reason code and 092 is the reject reason code.
5. The message gets mapped and the reject transaction gets created for the first payment, no new transaction gets created for the second payment.


6. The reject transaction gets created for the first payment.


7. No new transaction gets created for the second payment.


8. The audit trail for the first payment is updated as per below.


9. The `PSM.BLOB` application for the first payment is updated as per below.


10. Run the BNK/PAYMENT.STPFLOW.LIGHT service. The reject transaction moves to the 999 status and the original payment moves to the 998 status.


11. The audit trail of the reject transaction is provided below.


12. The accounting entries of the reject transaction are provided below.


13. The posting lines of the reject transaction are provided below.


14. The `POR.TRANSACTION` application for the reject transaction is updated as per below.


15. For the second payment, there is no change to the status code of the original payment, no update to the audit trail and to the `PSM.BLOB` application.
16. The audit trail for the second payment remains unchanged.


17. The `PSM.BLOB` application is not updated for the second payment.



[Process an Incoming Bulk Reject N03 for an Outward N06](#)

1. Process an outward N06 until it reaches the 999 status.
2. The details of the first payment are provided below.


3. The details of the second payment are provided below.


4. Process an inward bulk reject N03 message for the above payments.

   [](../../Resources/Images/India/PPINNP/Files/N03-BULK-034.txt)


5. The message gets mapped and the reject transaction gets created for both payments.


6. The reject transactions get created for the first payment.


7. The reject transactions get created for the second payment.


8. The audit trail for the first payment is updated as per below.


9. The `PSM.BLOB` application for the first payment is updated as per below.


10. The audit trail for the first payment is updated as per below.


11. The `PSM.BLOB` application for the first payment is updated as per below.


12. Run the BNK/PAYMENT.STPFLOW.LIGHT service.
13. The reject transactions for the firsts payment move to the 999 status and the original payment moves to the 998 status.


14. The reject transactions for the second payment move to the 999 status and the original payment moves to the 998 status.


15. The audit trail for the first reject transaction is provided below.


16. The accounting entries for the first reject transaction are provided below.


17. The posting lines for the first reject transaction are provided below.


18. The `POR.TRANSACTION` application for the first reject transaction is updated as per below.


19. The audit trail for the second reject transaction is provided below.


20. The accounting entries for the second reject transaction are provided below.


21. The posting lines for the second reject transaction are provided below.


22. The `POR.TRANSACTION` application for the second reject transaction is updated as per below.



## Support of 972 Start of Day and N04 End of Day

No outward messages will be sent to the SFMS system between the receipt of EOD messages (i.e. last batch of N04) and NEFT SOD message i.e. 972.

On reception of N04 and 972 message, TPH will store the details in a core CSR application and an enquiry is provided for the user to refer for both N04 and 972 message.

Payments generated during the EOD and SOD interval will be moved to the repair queue.

The following accounting entries will be posted for the payments released into the STP process for individual payments:

- DR. Customer account.
- CR. Nostro account.

Following will be the accounting entries for batch booking:

- DR. Customer account.
- CR. Suspense account.
- DR. Suspense account (individual payment instruction amount).
- CR. Nostro account (individual payment instruction amount).

[Process EOD Messages](#)

1. TPH receives a N04 EOD report.
2. Place a N04 message file in the following path: C:\Temenos\t24home\default\tcupload\INDNEFTCRS.


3. Run the BNK/EB.CREATE.FILE.UPLOAD and BNK/T24.UPLOAD.PROCESS services.
4. The file is processed and the Header Id is updated in the `EB.FILE.UPLOAD` application.


5. The file is uploaded in the `PP.CLR.REPORTS.FILE` application with the *Record Id* as "Transaction Date.Batch Time".
6. Navigate to the **India NEFT CRS Report** menu to access the `PP.CLR.REPORTS.FILE` application.


7. The clearing status is marked as Suspended in the INDNEFT record from the `PP.CLEARING` application.


8. Initiate an outgoing payment from POA after receiving the N04 EOD report from clearing.


9. Commit and authorise the payment.
10. The payment moves to the 4 status.


11. Run the medium service and the payment moves to the 235 status.


12. The audit trail is updated as per below.


13. No postings are done for the payment.


14. The error is provided below.



[Process SOD Messages](#)

1. Before receiving the SOD file, the *Clearing Status* in the INDNEFT record from the `PP.CLEARING` application is set as Suspended. Once SOD is received with sequence number 1, then the clearing status is changed to Blank(Active).


2. Process the SOD (972) file below. Place the SOD file inside the INDNEFT folder and put the file name in Payments.txt.

   [](../../Resources/Images/India/PPINNP/972_07.txt)

   [](../../Resources/Images/India/PPINNP/payments.txt)


3. Run the BNK/EB.CREATE.FILE.UPLOAD service.
4. The file will be upload in the `EB.FILE.UPLOAD` application.


5. Run the BNK/T24.UPLOAD.PROCESS service and two records will be created in the `PP.CLR.REPORTS.FILE` application.


6. The *Clearing Status* in the `PP.CLEARING` application will be changed to Blank(Active).


7. The database date is provided below.


8. The SOD date is provided below.


9. Initiate an outgoing payment from POA after receiving the 972 SOD report from clearing.


10. Authorise the record.
11. Run the medium service and the status will be updated to 235.


12. Release the record from the repair queue.


13. Commit and authorise the record.


14. The DVD and CVD of all payments will be imposed to the date in the latest 972 SOD report using the DATE Api.


15. The accounting entries are provided below.


16. The posting lines are provided below.


17. The “3380: Value date” tag in the outgoing message will be imposed to the date in latest 972 SOD using the EnrichOutMessageAPI in the `PP.CLEARING` application.



    [](../../Resources/Images/India/PPINNP/SOGEN22012000009.txt)

    [](../../Resources/Images/India/PPINNP/POR.SUPPLEMENTARY.INFO_1.pdf)

    [](../../Resources/Images/India/PPINNP/POR.TRANSACTION_1.pdf)

## Beneficiary Bank Acknowledgment Messages

For every N06 outward message sent out, the sending bank will receive an acknowledgment N10 message from the beneficiary bank confirming the beneficiary customer’s account has been credited.

When receiving a N10 message, TPH will search for the original message and update the `POR.AUDIT.TRIAL` application with a message as *Beneficiary Credited– Date and Time*.

If the original transaction is not available, N10 will be mapped and no action will be taken.

On receiving of an incoming N02 (credit transfer) message, TPH will generate an outgoing N10 message after crediting the beneficiary.

Outward N10 message will be generated for an incoming N02 (credit transfer) message using trip status API when the payment reaches 999 status.

The messageuserreference generated for N10 will be stored in the `POR.TRANSACTION` record of the inward N02.

In case of a negative response for a N10 message, the system will provide an option to regenerate the N10 message.

The same information which is sent out in an N10 message will be written in a local application. An enquiry has been released for this application using which the user can re-generate the N10 message with the same content.

[Process Beneficiary Bank Acknowledgment Messages for Outward N06 – Inward N10 Processing](#)

When a customer initiates a payment and TPH receives all positive acknowledgements, TPH will move the payment to the completed status.

TPH receives beneficiary bank acknowledgment message N10 and TPH will fetch the date and time when the beneficiary got credited from the N10 message and store it in the audit trail as *Beneficiary Credited – Date and Time* where the date and time is the value in the 3501: Amt Credited Time tag.

1. Initiate an outward N06 payment through POA.


2. The payment is updated with status 4 after committing and authorising the record.


3. Run the medium service and the payment moves to the 235 status.


4. Commit and authorise the payment from the repair screen and the payment moves to 600 status.


5. Run the medium service and the payment moves to the 687 status.


6. The outward N06 file is generated in the output folder.



   [](../../Resources/Images/India/PPINNP/SOGEN21105000006.txt)
7. The audit trail is provided below.


8. Process a F27 file for the payment.

   [](../../Resources/Images/India/PPINNP/F27.xml)
9. The file is received and mapped in the received file.


10. The audit trail is updated as per below.


11. Process a F20 file for the payment.

    [](../../Resources/Images/India/PPINNP/F20.xml)
12. The file is received and mapped in the received file.


13. The audit trail is updated as per below.


14. Process a F23 file for the payment.

    [](../../Resources/Images/India/PPINNP/F23.xml)
15. The file is received and mapped in the received file.


16. The payment moves to the 999 status.


17. The audit trail is updated as per below.


18. Process an inward N10 for the payment.

    [](../../Resources/Images/India/PPINNP/N10_76.txt)
19. Give the Messageuserreference value of N06 in the 2006 tag of the N10 file.
20. The file is received and mapped in the received file and bulk layer.


21. The audit trail is updated as per below.



[Acknowledgment Generation for Inward N02 Payments](#)

When processing an inward N02 individual file, TPH will process and map the transactions as individual payments will be created in non-STP mode. Postings will not be done at this stage and the payment status will be 235.

Once the N02 payment is manually released from the repair screen, the payment status moves to 999 and the following core accounting entries will be done by the system:

- DR. Nostro Account.
- CR. Customer Account.

After crediting the beneficiary, TPH will generate an outgoing N10 message.

1. Process a N02CT message through the INDNEFTInput folder.

   [](../../Resources/Images/India/PPINNP/N02_Individual-036.txt)
2. The message is received and mapped.


3. The message gets mapped in status 4.


4. On running the light service, the payment moves to the 235 status.
5. TPH will process and map the transactions as individual payment will be created in non-STP mode.


6. Postings will not be done at this stage.


7. Release the payment from the repair queue.


8. Approve the payment.


9. The payment status moved to 999.


10. The audit trail is updated as per below.


11. The accounting entries are provided below.


12. The posting lines are provided below.


13. An outward N10 message will be generated for an incoming N02 (credit transfer) message using the trip status API when the payment reaches the 999 status.

    [](../../Resources/Images/India/PPINNP/SOGEN21105000010.txt)


14. The messageuserreference generated for N10 will be stored in the `POR.TRANSACTION` record of the inward N02.



N10 is not applicable for N02RT.

[Regenerate an N10 Out-Message](#)

In case of a negative response for a N10 message, the user is able to regenerate the N10 message.

1. Process an inward N02 CT to the 999 status.

   [](../../Resources/Images/India/PPINNP/Files/N02CT_004.txt)


2. The generated N10 outfile is provided below.



   [](../../Resources/Images/India/PPINNP/Files/SOGEN21105000018.txt)
3. Process the F27 response as FBAPI.

   [](../../Resources/Images/India/PPINNP/Files/INDNEFT-F27-TPS170940200909-009-POS-03.xml)


4. A record will be created in the `CAINDR.ACK.RESUBMISSION` application with the *Receipt Status* as RJCT.


5. If the *Receipt Status* is RJCT, the user is able to re-genarate the outward N10 again.
6. The records that have the *Receipt Status* is RJCT are listed as per below.


7. Once the *Resubmit* option is selected as Yes, the out file will be generated and the receipt status and date will move to the previous receipt status and date.


8. The generated outfile after commiting the record is provided below.

   [](../../Resources/Images/India/PPINNP/Files/SOGEN21105000018_1.txt)
9. Once the record is committed for regeneration, then receipt status will be updated as NULL and waiting for the next ack message.

## Dates Calculation, Holiday and COB Check

If a payment is initiated on a weekend or public holiday, the payment will be processed with the processing date as the next available business day (Temenos Transact date). The debit value date and credit value date of the payment will be imposed as the date the payment was initiated.

[Initiated a Payment on a Weekend or Public Holiday](#)

1. The current system date is 14th Jan 2022 (holiday). The database date moved to next working date – 17th Jan 2022.


2. In the `HOLIDAY` application, 14th, 15th,16th are set as holidays.


3. The SOD date received is the 14th of January.


4. Initiate a pain.001 payment.


5. TPH will process the payment with the *Processing Date* as 17th Jan 2022 and DVD, CVD as 14th Jan 2022.


6. The audit trail is provided below.


7. The accounting entries are provided below.


8. The posting lines are provided below.


9. The `POR.TRANSACTION` dates are updated as per below.


10. The date in the 3380 tag of the outgoing N.06/N.07 is equal to 14th Jan 2022.



    [](../../Resources/Images/India/PPINNP/SOGEN22014000017.txt)

    [](../../Resources/Images/India/PPINNP/POR.SUPPLEMENTARY.INFO_2.pdf)

    [](../../Resources/Images/India/PPINNP/POR.TRANSACTION_2.pdf)

## Inward Payments and Inward Return Payments

For an inward payment, TPH will receive a N02 message. During a batch slot TPH can receive multiple N02 messages and a single N02 message can contain multiple credit transfers and return messages. TPH will de-bulk the payment and create individual transactions for all the payments in non-STP mode.

For all rejected payments sent by clearing, TPH will receive an individual N03 rejection message before the end of the batch. TPH will mark these payments as canceled. At the end of the batch TPH will receive a N04 report message. On the reception of a N04 message, TPH will cross check the total amount and count of the entire CT and RT in the N04 with the total amount and count of all the payments received in that match. If it is a match, TPH will move all the payments in the particular batch which are not rejected to completed status. If it is a mismatch all payments in the particular batch will remain in 235 status.

On the reception of the N04 end of day, TPH will calculate the sum of total amount and total count in all the payments received in the day. This sum of total amount and count should be matched against the sum of total amount and count of entire CT and RT in the EOD report. If it matches, all the pending transactions in the previous batches and all pending transactions in the current batch should be processed through STP flow. If there is a mismatch, leave all the transactions in that batch and previous batches in 235 status itself. The user then has to take manual action against these payments

The following core accounting entries will be done by the system:

- DR. Nostro Account.
- CR. Customer Account.

For inward return payments, a return transaction will be created in non-STP mode and on receipt of the N04 batch message the accounting entries of the original transaction will be reversed.

[Receive an Individual N.02 CT Payment](#)

1. TPH receives an N.02 message with a single CT payment.

   [](../../Resources/Images/India/PPINNP/N02_Individual-001.txt)
2. TPH will process and map the transactions and individual payment will be created in non-STP mode.


3. The message gets mapped in status 4.


4. Run the light service. The payment moves to the 235 status.


5. The audit trail of the payment is provided below.


6. No postings are done.


7. View the repair queue.



[Receive a Bulk N.02 CT Payment](#)

1. TPH receives multiple N.02s for a batch, each N.02 has multiple CT payments.

   [](../../Resources/Images/India/PPINNP/N02_NEFTBULK-001.txt)
2. TPH will process and map the file.


3. TPH will debulk the file and map the transactions as individual payments. The message gets mapped at status 4.


4. Run the service and the payments will be moved to the 235 status.


5. The audit trail is provided below.


6. No postings are done.


7. View the repair queue.



[Receive an N.02 Message with both CT and RT Payments](#)

1. TPH receives an N.02 message with both CT and RT payments.

   [](../../Resources/Images/India/PPINNP/N02CT_N02RT - 001.txt)
2. The message gets mapped in status 4. Two transactions are created.


3. Run the light service and the payment will be moved to the 235 status.


4. The inward CT payment is provided below.


5. View the repair queue.



   [](../../Resources/Images/India/PPINNP/POR.SUPPLEMENTARY.INFO BNK21105KFGKFMHM.pdf)

   [](../../Resources/Images/India/PPINNP/POR.TRANSACTION BNK21105KFGKFMHM.pdf)
6. The inward RT along with the original payment is provided below.


7. View the repair queue.



   [](../../Resources/Images/India/PPINNP/POR.SUPPLEMENTARY.INFO BNK21105HFKH0HKK.pdf)

   [](../../Resources/Images/India/PPINNP/POR.TRANSACTION BNK21105HFKH0HKK.pdf)

[Receive an Individual N02 RT Payment](#)

1. Place an N02RT message with a single transaction in the INDNEFTInput folder.

   [](../../Resources/Images/India/PPINNP/N02RT_012.txt)
2. TPH will identify the original transaction using the “2006: Related Reference Number” tag of the N02 message. The message gets mapped in status 4.


3. For inward return payments, a return transaction will be created in non-STP mode.
4. Run the light service and the payment will be moved to the 235 status.


5. The audit trail of the payment is provided below.


6. No postings are done at this stage.


7. View the repair queue.


8. The POR.SUPPLEMENTARY.INFO details are provided below.


9. The POR.TRANSACTION details are provided below.


10. Commit the payment from the repair queue and the payment moves to the 999 status.
11. The `POR.TRANSACTION` application is updated and the N10 event is not generated.

[Receive a Bulk N02 RT Payment](#)

1. TPH receives an N.02 message with bulk RT payment.


2. All bulk transactions are mapped as separate transactions at status 4.


3. Run the service and the payments will be moved to the 235 status.


4. The payment amount is 851.


5. The audit trail of the first payment is provided below.


6. No postings are done.


7. View the repair queue.


8. The second payment amount is 852.


9. The audit trail is provided below.


10. No postings are created.


11. View the repair queue.



[Inward N04 Processing - Matching of Inward N02 with N04 and Moving the Payment to Complete](#)

1. Process an inward NO2 individual file.

   [](../../Resources/Images/India/PPINNP/N02_Individual-025.txt)


2. On running light service payment moves to the 235 status.


3. The audit trail is provided below.


4. No accounting entries are generated.


5. Upload an Inward N.04 –EOB file.
6. Place payment file in the tcupload folder and place NO4.txt file within INDNEFTCRS folder.


7. Run the BNK/EB.CREATE.FILE.UPLOAD and the BNK/T24.UPLOAD.PROCESS services and a record will create in the `EB.FILE.UPLOAD` application.


8. Records will create in `PP.CLR.REPORTS.FILE` application. One header and the number of transactions according to input file records will be create in the `PP.CLR.REPORTS.FILE` application.
9. The HEADER record will have the default record *Id*.
10. The ITEM record will have the record *Id* as DATE.<BATCH.TIME> from the NO4.txt file.


11. The Header details are provided below.


12. The Item details are provided below.


13. Check the batch time of the N.04 –EOB file and the customer reference of N02 and other transaction details.


14. If the batch time and other transaction details of the N04-EOB file matches with the customer reference and the transaction details of the N02 file, manually release the payment from the repair queue.


15. Commit and authorise the record.


16. The payment moves to the 999 status.


17. The audit trail is provided below.


18. The following core accounting entries will be done by the system:
    - DR. Nostro/Suspense Account.
    - CR. Customer Account.



    [](../../Resources/Images/India/PPINNP/POR.SUPPLEMENTARY.INFO_3.pdf)

    [](../../Resources/Images/India/PPINNP/POR.TRANSACTION_3.pdf)

[Match an N04 End of Batch Report with N02](#)

TPH can receive multiple N02s for a batch in a single session. Each N.02 has multiple CT payments. TPH receives the N04 EOB report message from clearing for the entire N02s received for that batch. On reception of the N04 EOB, the system will check for which batch the N04 is received.

The system will identify the corresponding record and cross check the total amount and count of the entire CT in N04 with the total amount and count of batch.

- If there is no mismatch all the payments in the corresponding batch will be processed through the STP flow.
- If there is a mismatch, all the payments in the corresponding batch will not be processed and remain in the 235 status.

[Positive Scenario (Credit Transfer)](#)

1. TPH receives an N02CT payment. The payment is marked at status 4.




2. Run the light service and the payment moves to the 235 status.


3. The audit trial is updated as per below.


4. There are no posting lines and accounting entries.


5. Upload the N04 EOB file. On reception of the N04 EOB, the batch service will calculate the sum of total amount and total count in all the records in the local back-end file.
6. This sum of total amount and count will be matched against the sum of total amount and count of the entire CT and RT in the EOB report. If there is no mismatch, all the payments in the corresponding batch will be processed through the STP flow and the following core accounting entries will be done by the system:
   - DR. Nostro Account.
   - CR. Customer Account.
7. Place the payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.

   [](../../Resources/Images/India/PPINNP/Files/payments_1.txt)

   [](../../Resources/Images/India/PPINNP/Files/N04-1558.txt)
8. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


9. The concat file can be viewed for the transaction by using the LIST-ITEM F.PPINNP.CONCAT.DETS request.


10. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


11. The concat file will have the status updated as completed.


12. The details can be viewed in the `PP.CLR.REPORTS.FILE` application.


13. If the batch time and the other transaction details of the N04-EOB file matches with the customer reference and transaction details of the N02 file, the payment will be released automatically.
14. Run the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service and the payment moves to the 600 status.
15. Run the light service and the payment moves to the 999 status.


16. The audit trial is updated as per below.


17. The posting lines are updated as per below.


18. The accounting entries are updated as per below.



[Negative Scenario (Credit Transfer)](#)

1. TPH receives an N02CT payment. The payment is marked at status 4.

   [](../../Resources/Images/India/PPINNP/Files/N02CT_1141.txt)

   [](../../Resources/Images/India/PPINNP/Files/N02CT_1141-1.txt)


2. Run the light service. The payment moves to the 235 status.


3. Upload an N04 EOB file.
4. Place the payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.

   [](../../Resources/Images/India/PPINNP/Files/N04-11411.txt)

   [](../../Resources/Images/India/PPINNP/Files/payments_2.txt)
5. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


6. The concat file can be viewed for the transaction by using the LIST-ITEM F.PPINNP.CONCAT.DETS request.


7. Run the BNK/T24.UPLOAD.PROCESS service and a record will be processed in the `EB.FILE.UPLOAD` application.


8. The details can be viewed in the `PP.CLR.REPORTS.FILE` application.


9. View the concat file. Since there is mismatch in the amount, the status is updated as Pending.


10. The payments will remain in the 235 status.



[Match an N04 End of Day Report with N02](#)

For an inward payment, TPH will receive a N02 message. During a batch slot TPH can receive multiple N02 messages and a single N02 message can contain multiple credit transfers and return messages.

On reception of the EOD message, the count and amount needs to be reconciled. If ALL the data matches, then the N02 messages that are received as part of the batch that are marked as pending in the previous batches will be automatically released for STP processing. If data doesn't match, then the EOD status will be updated as pending.

[Positive Scenario](#)

An example is provided below for N04 EOD report processing.

It is assumed that the N04 EOD contains all the pending transactions in the previous batches and all pending transactions in the current batch.

On reception of the N04 EOD, a record will be created in the back end file with the summation of count and total amount of each file received in the batch.

This sum of total amount and count will be matched against the sum of total amount and count of the entire CT and RT in the EOD report.

Since N04 has all the pending transactions in the previous batches and all the pending transactions in the current batch, it will be processed through the STP flow.

1. All the previous batches are settled down.


2. The last batch (batch 1047) has three CT transaction and one RT transaction in total (as perbelow). The EOB file received total amount doesn’t matches witht the total sum in the 1047 batch, hence all the txns are in 235 status.
3. The details of the outward N06 payment are provided below.


4. The outward N06 file is provided below.

   [](../../Resources/Images/India/PPINNP/Files/SOGEN22109000051.txt)
5. Process an incoming N02 file with one RT transaction the matches with the above transaction and then have three CT transactions in it.

   [](../../Resources/Images/India/PPINNP/Files/N02_CT_RT_018.txt)


6. The transactions highlighted in yellow are RT transactions(original and return) and the transactions highlighted in green are CT transactions.
7. The concat details are provided below.


8. Process a EOB that doesn’t match with the above sums.

   [](../../Resources/Images/India/PPINNP/Files/N04_EOB_1047.txt)


9. As the total EOB doesn’t match with the total sum, the EOB is marked as Pending.
10. The unmatched payments are listed in the Daily Clearing Report enquiry.


11. The `PP.CLEARING` record is still in Active status.


12. Now that the EOD is the final batch of the day, two CT and one RT transaction are processed as per below.


13. The outward N06 file is provided below.

    [](../../Resources/Images/India/PPINNP/Files/SOGEN22109000052.txt)
14. Process the inward N02 file that has two CT and one RT transaction that matches with the above transaction.

    [](../../Resources/Images/India/PPINNP/Files/N02_CT_RT_019.txt)


15. The transaction highlighted in yellow refer to the RT and the transactions highlighted in blue refer to the incoming batch transaction.
16. The customer reference is 20220419.EOD which refers to the transaction received in EOD.
17. Below is the concat file updated after processing the incoming N02.


18. Process an EOD with total Ct transaction as 5 (three in batch 1047 and two in EOD ) with the total sum of 2780.09 (batch pending + EOD pending transaction sum).
19. Also the EOD file has the total RT transaction as two (one in batch 1047 and one in EOD) with the total sum of 1894.38(batch pending + EOD pending transaction sum).
20. The list of pending batch and EOD payments is provided below.


21. Process the below N04 files that matches with the above total CT and RT sum.

    [](../../Resources/Images/India/PPINNP/Files/N04_EOD_014.txt)


22. The transaction details after receiving the EOD are provided below.


23. The transaction highlighted in the red box are part of EOD and the transactions highlighted inside black box are transaction part of EOB.
24. As the overall total sum of the batch and EOD matches, all the transactions move to STP for further processing.
25. The details of the cancat file after processing EOD that matches completely are provided below.


26. All the CT transactions in BATCH and EOD move to the 999 status, and all the RT transaction received in BATCH and EOD move to the 999 status, marking the original txn to 996.


27. A sample CT transaction is provided below.


28. A sample RT transaction is provided below.


29. The enquiry below shows that there are no unmatched payments.



[Negative Scenario](#)

1. For an existing successful N02CT batches, process an EOD batch. The payments will remain in the 235 status due to an EOD mismatch.
2. Ensure that successful N02CT already exist.

   [](../../Resources/Images/India/PPINNP/Files/N02CT_1111.txt)

   [](../../Resources/Images/India/PPINNP/Files/N02CT_1112.txt)

   [](../../Resources/Images/India/PPINNP/Files/N04_1111.txt)

   [](../../Resources/Images/India/PPINNP/Files/N04CT1_1112.txt)


3. The existing payment batches should be in completed status.


4. Process the N02CT file for the EOD batch. Run the light service to move the payment to the 235 status. Make sure the *Batch Num* is given as EOD.

   [](../../Resources/Images/India/PPINNP/Files/N02CT_EOD.txt)


5. The concat record will be created with the session id (LIST-ITEM F.PPINNP.CONCAT.DETS), containing the details of the payment of the last batch.


6. Process the N04 for the EOD batch containing incorrect details for the current batch.

   [](../../Resources/Images/India/PPINNP/Files/payments_4.txt)

   [](../../Resources/Images/India/PPINNP/Files/N04_EOD_CT.txt)
7. Run the BNK/EB.CREATE.FILE.UPLOAD and BNK/T24.UPLOAD.PROCESS services.


8. The following records are created for the N04 EOD file.


9. The payment *Concat Id* is modified and the status is updated as pending in the concat file due to mismatch of details.


10. The EOD batch payments remain in the 235 status.



## Outward Returns

For an inward credit transfer, if there is an issue with the credit account, other than posting restriction, TPH will automatically return the inward CT by generating an N07 message and the payment will be moved to status 687 and the original transaction will be reversed.

The following set of accounting entries will be done by the system:

- DR. Nostro Account.
- CR. Return Suspense Account.
- DR. Return Suspense Account.
- CR. Nostro Account.

Once the N07 payment is generated, TPH will receive the settlement acknowledgement messages.

In case of negative acknowledgement, the payment will be moved to the `PP.ORDER.ENTRY,REPAIR.INDIA.NEFT` repair queue.

TPH will not be receiving any N03 reject messages or N10 messages for outward returns.

[Outward Return (N07) for Inward Credit Transfer (N02CT) (Manual/Automatic)](#)

When a credit account is invalid or closed or inactive, TPH will automatically return the inward CT by generating an N07 message after the receipt of the EOB message.

When a credit account has posting restrictions, TPH will keep the payment in the 235 status even after the receipt of EOB/EOD.

[Scenario 1](#)

TPH receives an inward N02CT bulk payment which has a combination of valid and invalid payments. The payment moves to the 235 Non-STP indicator. N04 EOB is received for the batch. The concat is marked to completed. Payments are still in 235 status. When the release suspended payments service is run, the valid payments are released and moved to the 600 status. Invalid payments remain in 235 status. When the user manually returns the invalid payments, the original payment moves to the 996 status and a return payment is created and moved to the 687 status. Payments that are valid move to the 999 status.

1. Push an N02CT message in the INDNEFTInput folder.
2. By running the light service it will move from status 4 to status 235.


3. Upload an N04 EOB file. Place payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
4. Place the N04 file in the below mentioned path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.



   [](../../Resources/Images/India/PPINNP/Files/N04-1162.txt)
5. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


6. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


7. The concat file can be viewd for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


8. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


9. The concat file can be viewed again, with the status updated as Completed.


10. Run the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service and the payments will be released. Payments with CPD20057 error will remain in status 235 and only the payments with PDE20001 will move to the 600 status.


11. Return the payments which are in 235 status by giving a return reason.


12. Authorise the payment.


13. The final payment status after running the light service is provided below.





[Scenario 2](#)

TPH receives an inward N02CT. The payment moves to 235 status due to account restriction and Non-STP indicator. An N04 EOB is received for the batch. The concat is marked as pending and the payment is still in 235 status. When the user manually returns the payment, the original payment moves to the 996 status and a return payment is created and moved to the 687 status.

1. Push the message in the INDNEFTInput folder, it will be mapped as status 4.


2. After running the BNK/PAYMENT.STPFLOW.LIGHT service, it will move to the 235 status.


3. The audit trail is provided below.


4. Upload an N04 EOB file.
5. Place payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
6. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

   [](../../Resources/Images/India/PPINNP/Files/N04-1131.txt)
7. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


8. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


9. The concat can be viewed for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


10. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


11. The concat file can be viewed again, with the status updated as pending.


12. Return the payment which is in 235 status by giving a return reason.


13. Authorise it.


14. The payment will move to the 20 status and after running the light service it will move to the 988 status.


15. The return payment will be generated with status 4 and after running the light service it will move to the 687 status.



    [](../../Resources/Images/India/PPINNP/Files/Payment Information - Model Bank.html)

    [](../../Resources/Images/India/PPINNP/Files/Payment Information - Model Bank996.html)
16. An event is generated in the `IF.EVENTS.INTERFACE.TABLE` application as per below.


17. The outward N07 file will be generated in the INDNEFTOutput folder.

    [](../../Resources/Images/India/PPINNP/Files/SOGEN22109000011.txt)

[Scenario 3](#)

TPH receives an inward N02CT. The payments move to the 235 status due to account restriction and Non-STP indicator. N04 EOB is received for the batch. The concat is marked as pending then EOD is processed which is marked as completed. After running the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service, the payments without any account restriction move to the 600 status and the payments with account restriction will stay in the 235 status. After running the light service the payment in status 600 will move to the 999 status and the payment in 235 status will remain the same.

1. Push an N02CT message in the INDNEFTInput folder.
2. By running the light service it will move to the 235 status.


3. The audit trail of the payment without any account restrictions is provided below.


4. The audit trail of the second payment with account restrictions is provided below.


5. Upload an N04 EOB file (PENDING).
6. Place payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
7. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

   [](../../Resources/Images/India/PPINNP/Files/N04-1167.txt)
8. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


9. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


10. The concat file can be viewed for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


11. Run the BNK/T24.UPLOAD.PROCESS and the record will be processed in the `EB.FILE.UPLOAD` application.


12. The concat can be viewed again, with the status updated as PENDING.


13. Push an N02CT with EOD batch.
14. Run the light service and the payment status will move from 4 to 235.


15. Upload an N04 EOD file (COMPLETED).
16. Place payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.


17. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

    [](../../Resources/Images/India/PPINNP/Files/N04-EOD.txt)
18. After receiving the EOD file, TPH will change the status to suspended in the `PP.CLEARING` application.


19. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


20. The concat file can be viewed for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


21. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


22. The concat can be viewed again with the status updated as Completed for EOB and EOD payment also.


23. Release the payment by running the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service.
24. The payment with posting restriction will stay in the 235 status, and the payment without account restriction will move to the 600 status.


25. By running the light service, the payments in 600 status will move to the 999 status.



[Scenario 4](#)

TPH receives an inward N02CT. Payments move to the 235 status due to account restriction and Non-STP indicator. N04 EOB is received for the batch. The concat file is marked as completed then EOD is processed which is marked as Pending. After running the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service, the payments without any account restriction move to the 600 status and the payments with account restriction will stay in the 235 status. After running the light service, the 600 status payment will move to the 999 status and the 235 payment will remain in the 235 status.

1. Push an N02CT message in the INDNEFTInput folder.
2. After running the light service, it will move from status 4 to the 235 status.


3. Upload a N04 EOB (completed) file:
4. Place payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
5. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

   [](../../Resources/Images/India/PPINNP/Files/N04-1168.txt)
6. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


7. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


8. The concat file can be viewed for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


9. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


10. The concat file can be viewed again, with the status updated as Completed.


11. Run the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service and the payments will be released. The payments with CPD20057 error will remain in the 235 status and only the ones with PDE20001 will move to the 600 status.


12. Run the light service and the payment in 600 status moves to the 999 status and the 235 payment remains in the 235 status.


13. Upload a N04 EOD(PENDING) file.
14. Push the N02CT message in the INDNEFTInput folder with the batch number as EOD.
15. By running the light service it will move from 4 to the 235 status.


16. Place the payment.txt file in the tcupload folder and place the inward N04 EOD file in the INDNEFTCRS folder.
17. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

    [](../../Resources/Images/India/PPINNP/Files/N04-EOD2.txt)
18. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


19. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


20. The concat file can be viewed for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


21. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


22. The concat file can be viewed again, with the status updated as PENDING.


23. Run the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service and the payments will be released. Payments with the CPD20057 error will remain in the 235 status and only the ones with PDE20001 will move to the 600 status and after running the light service they will move to the 999 status.
24. Here, for the EOD pending case, both payments are in the 235 status because the amount is not released.
25. The final status of the payments of the day is provided below.


26. After receiving the EOD file, the status of clear status in the `PP.CLEARING` application will marked as suspended.



[Scenario 5](#)

TPH receives an inward N02CT. Payments move to the 235 status due to account restriction and Non-STP indicator. N04 EOB is received for the batch. The concat is marked as pending then EOD is processed which is marked as pending. After running the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service, no payments get released and they stay in the 235 status.

Payments that are in mismatch status, after processing EOD(PENDING), should be seen in the INDNEFT.N04.MANU.PROCESSING enquiry.

After receiving EOD file, the clearing status is marked as suspended in the `PP.CLEARING` application. If the user tries to process the N07 file after the clearing status is marked as suspended, the payment will not be processed and the outward file will not be generated.

1. Push an N02CT message in the INDNEFTInput folder.


2. Upload the N04 EOB(PENDING) file.
3. Place the payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
4. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.


5. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


6. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


7. The concat file can be viewed for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


8. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


9. The concat can be viewed again, with the status updated as PENDING.


10. Run the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service and the payments will stay in the 235 status because the amount is in pending status.


11. Push the N02CT message in the INDNEFTInput folder.
12. By running the light service it will move from 4 to the 235 status.


13. Upload a N04 EOD (PENDING) file.
14. Place payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
15. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

    [](../../Resources/Images/India/PPINNP/Files/N04-EOD3.txt)
16. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


17. Run the BNK/EB.CREATE.FILE.UPLOAD service and the record will be created in the `EB.FILE.UPLOAD` application.


18. The concat can be viewed for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


19. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


20. The concat can be viewed again, with the status updated as PENDING.


21. Run the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service and the payments will not be released and they will stay in the 235 status.


22. After receiving the EOD file, the status will be changed to Suspended in the `PP.CLEARING` application.


23. The payments that are in the mismatch status after processing EOD(PENDING) can be seen in the INDNEFT.N04.MANU.PROCESSING enquiry.
24. The concat of the payments is shown as PENDING below.


25. They will stay in the 235 status.


26. These pending payment can be viewed using the INDNEFT.N04.MANU.PROCESSING enquiry.


27. After receiving the EOD file, the clearing status is marked as Suspended in the `PP.CLEARING` application. If the user tries to process a N07 file after the clearing status is marked as Suspended, the payment will not be processed and the outward file will not be generated.
28. Due to the EOD mismatch, the payment remains in the 235 status.


29. Return the 235 status payment by giving the reason in the repair screen.


30. Authorise it.


31. Run the light service and the original payment will move to the 988 status.


32. And the return payment moves to the 235 status.


33. The audit trail is provided below.



[Scenario 6](#)

TPH receives an inward N02CT. The payments move to the 235 status due to account restriction and Non-STP indicator. N04 EOB is received for the batch. The concat is marked as completed then EOD is processed which is marked as completed . After running the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service, the payments without any account restriction move to the 600 status and the payments with account restriction will stay in the 235 status. After running the light service, the payment in 600 status will move to the 999 status and the 235 payment will remain in the 235 status.

1. Push the N02CT message in the INDNEFTInput folder.
2. By running the light service it will move from 4 to 235 status.


3. Upload a N04 EOB(COMPLETED) file.
4. Place payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
5. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

   [](../../Resources/Images/India/PPINNP/Files/N04-1170.txt)
6. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


7. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


8. The concat file can be viewd for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


9. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


10. The concat can be viewed again, with the status updated as Completed.


11. Run the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service and the payments will be released. Payments with the CPD20057 error will remain in the 235 status and only the ones with PDE20001 will move to the 600 status.


12. Run the light service and the payment which is in 600 status will move to the 999 status.


13. Push the N02CT message in the INDNEFTInput folder.
14. By running the light service, it will move from 4 to the 235 status.


15. Upload a N04 EOD(COMPLETED) file.
16. Place the payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
17. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

    [](../../Resources/Images/India/PPINNP/Files/N04-EOD4.txt)
18. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


19. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


20. The concat can be viewed for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


21. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


22. The concat can be viewed again with the status updated as Completed.


23. Run the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service and the payments will be released. Payments with the CPD20057 error will remain in the 235 status and only the ones with PDE20001 will move to the 600 status.


24. Run the light service and the payment in 600 status will move to the 999 status.


25. The final status of all the payments of the day is provided below.


26. When the EOD file is processed, the status in the `PP.CLEARING` application will change to Suspended.



[Scenario 7](#)

N02ct- NON-STP + account restriction - 235 - N04 EOB completed -  235 - enquiry  to  manually return - N02 996 / N07 687 .TPH receives an inward N02CT. The payment moves to the 235 status due to account restriction and Non-STP indicator. N04 EOB is received for the batch. The concat is marked as completed. The payment is still in 235 status. When the user manually returns the payment, the original payment moves to the 996 status and the return payment is created and moves to the 687 status.

1. Push the N02CT message in the INDNEFTInput folder.
2. By running the light service it will move to the 235 status.


3. The audit trail is provided below.


4. Upload a N04 EOB file.
5. Place the payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
6. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

   [](../../Resources/Images/India/PPINNP/Files/N04-1157.txt)
7. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


8. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


9. The concat can be viewed for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


10. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


11. The concat can be viewed again with the status updated as Completed.


12. Return the payment which is in 235 status by giving a return reason.


13. Authorise the payment.


14. The original payment will change to 20 and by running the light service it will move to the 996 status and the return payment moves to the 687 status.



[Scenario 8](#)

Process an Inward N02 CT with invalid account details. The payment moves to the 235 status due to invalid account and Non-STP indicator. N04 EOB is received for the batch. The concat is marked as completed. Run the release suspended service and the original payment moves to the 996 status and the return payment is created and moves to the 687 status.

1. Push the message in the INDNEFTInput folder, it will be mapped in status 4.


2. After running the BNK/PAYMENT.STPFLOW.LIGHT service, it will move to the 235 status.


3. The audit trail is provided below.


4. Upload an N04 EOB file.
5. Place the payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
6. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

   [](../../Resources/Images/India/PPINNP/Files/N04-1423.txt)
7. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


8. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.
9. Run the BNK/T24.UPLOAD.PROCESS and the record will be processed in the `EB.FILE.UPLOAD` application.
10. The concat can be viewed through the LIST-ITEM F.PPINNP.CONCAT.DETS, it will be marked as complete.


11. Run the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service and the payment will move to the 20 status.


12. After running the BNK/PAYMENT.STPFLOW.LIGHT service, the payment will be automatically returned.
13. The original payment will be in the status 996.


14. The audit trail of the original payment is provided below.


15. The return payment will be in the status 687.


16. Run the integration service.

    [](../../Resources/Images/India/PPINNP/Files/SOGEN22109000026.txt)

[Scenario 9](#)

Process an Inward N02 CT with invalid account details. The payment moves to the 235 status due to account closed and Non-STP indicator. N04 EOB is received for the batch. The concat file is marked as completed. Run the release suspended service and the original payment moves to the 996 status and the return payment is created and moves to the 687 status.

1. Push the message in the INDNEFTInput folder, it will be mapped with status 4.


2. After running the BNK/PAYMENT.STPFLOW.LIGHT service, it will move to the 235 status.


3. The audit trail is provided below.


4. Upload a N04 EOB file.
5. Place the payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
6. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

   [](../../Resources/Images/India/PPINNP/Files/N04-1777.txt)
7. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


8. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.
9. Run the BNK/T24.UPLOAD.PROCESS and the record will be processed in the `EB.FILE.UPLOAD` application.
10. The concat file can be viewed through the LIST-ITEM F.PPINNP.CONCAT.DETS, it will be marked as complete.


11. Run the BNK/CAINDR.RELEASE.SUSPENDED.PYMNTS service and the payment will be moved to the 20 status.


12. After running the BNK/PAYMENT.STPFLOW.LIGHT service, the payment will be automatically returned.
13. The original payment will be in the status 996.


14. The audit trail of the original payment is provided below.


15. The return payment will be in the status 687.


16. Run the integration service.

    [](../../Resources/Images/India/PPINNP/Files/SOGEN22109000027.txt)

[ADMI Flow for Outward N07](#)

For an inward credit transfer, if there is an issue with the credit account TPH will automatically return the inward CT by generating an N07 message and the payment will move to status ‘687’. The original transaction will be reversed. Positive and negative ADMI messages are received for N07.

[Scenario 1](#)

TPH receives an inward N02CT. The payment moves to the 235 status due to account restriction and Non-STP indicator. N04 EOB is received for the batch. The concat is marked as pending. The payment is still in 235 status. When the user manually returns the payment, the original payment moves to the 996 status and the return payment is created and moves to the 687 status.Positive F series is received.

1. Push the message in the INDNEFTInput folder, it will be mapped weith status 4.


2. After running the BNK/PAYMENT.STPFLOW.LIGHT service, it will move to the 235 status.


3. The audit trail is provided below.


4. Upload a N04 EOB file.
5. Place the payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
6. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

   [](../../Resources/Images/India/PPINNP/Files/N04-1132.txt)
7. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


8. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


9. The concat can be viewed for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


10. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


11. The concat can be viewed again with the status updated as pending.


12. Return the payment which is in 235 status by giving a return reason.


13. Authorise it.


14. The payment will move to the 20 status and after running the light service it will move to the 988 status.


15. The return payment will be generated with status 4 and after running the light service it will move to the 687 status.


16. An event is created in the `IF.EVENTS.INTERFACE.TABLE` application.


17. The outward N07 file will be generated in the INDNEFTOutput folder.

    [](../../Resources/Images/India/PPINNP/Files/SOGEN22109000014.txt)
18. The `PSM.BLOB` application is updated as per below.


19. Push F Series messages.
20. Now process the inward F27 Ack message {A:CBSF27I000000018SBIN0000002202104151325PBAPI000000XX}.

    [](../../Resources/Images/India/PPINNP/Files/F27-1.xml)
21. The message gets mapped as per below.




22. The `PSM.BLOB` application gets updated as per below.


23. The payment remains in the 687 status.


24. The audit trail gets updated as per below.


25. Process an inward F20 message {A:CBSF20O000000018SBIN0001001202104151325}.

    [](../../Resources/Images/India/PPINNP/Files/F20.xml)
26. The message gets mapped as per below.




27. The `PSM.BLOB` application is updated as per below.




28. The audit trail is updated as per below.


29. Process the inward F23 message {A:CBSF23O000000018SBIN0001001202104151325}.

    [](../../Resources/Images/India/PPINNP/Files/F23.xml)
30. The message gets mapped as per below.




31. The `PSM.BLOB` application gets updated as per below.


32. The payment moves to the 999 status.


33. The audit trail gets updated as per below.



[Scenario 2](#)

TPH receives an inward N02CT. The payment moves to the 235 status due to account restriction and Non-STP indicator. N04 EOB is received for the batch. The concat is marked as pending. The payment is still in 235 status. When the user manually returns the payment, the original payment moves to the 996 status and the return payment is created and moves to the 687 status.Negative F series is received.

1. Push the message in the INDNEFTInput folder, it will be mapped with status 4.


2. After running the BNK/PAYMENT.STPFLOW.LIGHT service, it will move to the 235 status.


3. The audit trail is provided below.


4. Upload n N04 EOB file.
5. Place the payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.
6. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

   [](../../Resources/Images/India/PPINNP/Files/N04-1136.txt)
7. Place the Payment.txt file in the following path: C:\UTP\Temenos\t24home\default\tcupload.


8. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


9. The concat can be viewed for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


10. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


11. The concat can be viewed again with the status updated as pending.


12. Return the payment which is in 235 status by giving a return reason.


13. Authorise it.


14. The payment will move to the 20 status and after running the light service it will move to the 988 status.






15. The return payment will be generated with status 4 and after running the light service it will move to the 687 status.


16. The audit trail is provided below.


17. An event is created in the `IF.EVENTS.INTERFACE.TABLE` application.


18. The outward N07 file will be generated in the INDNEFTOutput folder.

    [](../../Resources/Images/India/PPINNP/Files/SOGEN22109000018.txt)


19. The `PSM.BLOB` application is updated as per below.


20. Push F Series messages.
21. Now process the inward F27 NAck message: {A:CBSF27I000000021SBIN0000002202104151325FBAPI000000XX}.



    [](../../Resources/Images/India/PPINNP/Files/F27-RJCT.xml)
22. The message gets mapped as per below.




23. The `PSM.BLOB` application gets updated as per below.


24. The payment remains in 687 status and after running the service it will move to the 988 status and a new settlement payment will be generated with status 4.








25. Run the BNK/PAYMENT.STPFLOW.LIGHT service and the settlement transaction moves to the 999 status and the original payment moves to the 998 status.


26. The record details are provided below.


27. The audit trail is updated as per below.


28. The posting lines are provided below.


29. The accounting entries are provided below.


30. The final status of the original payment is provided below.


31. The final status of the returned payment is provided below.


32. The final status of the settlement payment is provided below.



[Scenario 3](#)

TPH receives an inward N02CT. The payment moves to the 235 status due to account restriction and Non-STP indicator. N04 EOB is received for the batch. The concat is marked as pending. The payment is still in 235 status. When the user manually returns the payment, the original payment moves to the 996 status and the return payment is created and moves to the 687 status.Negative F series is received.

1. Push the message in the INDNEFTInput folder, it will be mapped with status 4.


2. After running the light service, the payment will move to the 235 status.


3. Upload an EOB file.
4. Place the payment.txt file in the tcupload folder and place the inward N04 EOB file in the INDNEFTCRS folder.


5. Place the N04 file in the following path: C:\UTP\Temenos\t24home\default\tcupload\INDNEFTCRS.

   [](../../Resources/Images/India/PPINNP/Files/N04-1140.txt)
6. Run the BNK/EB.CREATE.FILE.UPLOAD service and a record will be created in the `EB.FILE.UPLOAD` application.


7. The concat can be viewed for the transaction by using LIST-ITEM F.PPINNP.CONCAT.DETS.


8. Run the BNK/T24.UPLOAD.PROCESS service and the record will be processed in the `EB.FILE.UPLOAD` application.


9. The concat can be viewed again with the status updated as pending.


10. Return the payment which is in 235 status by giving a return reason.


11. Authorise it.


12. By running the light service, the original payment will be moved to the 996 status and the return payment will be generated and moved to the 687 status.


13. An event is created in the `IF.EVENTS.INTERFACE.TABLE` application.


14. Run the integration service and the outward file will be generate in the INDNEFTOutward folder.

    [](../../Resources/Images/India/PPINNP/Files/SOGEN22109000023.txt)
15. Push F Series messages.
16. Now process the inward F27 Ack message: {A:CBSF27I000000025SBIN0000002202104151325PBAPI000000XX}.


17. The `PSM.BLOB` application gets updated as per below.


18. The audit trail gets updated as per below.


19. The payment is in 687 status.


20. Process an inward F27 PBAPI message and the `PSM.BLOB` application will be updated.
21. Process an inward F25 NACK message: {A:CBSF25O000000025SBIN00010012021041513252105XXXXXXXXX}.

    [](../../Resources/Images/India/PPINNP/Files/F25-n-.xml)
22. The audit trail gets updated as per below.


23. The settlement payment will be created with status 4 and after running the light service it will move to the 999 status.


24. The `PSM.BLOB` application gets updated as per below.


25. The OE view is provided below.


26. The audit trail gets updated as per below.


27. The posting lines are provided below.


28. The accounting entries are provided below.


29. The final status of the original payment is provided below.


30. The final status of the return payment is provided below.


31. The final status of the settlement payment is provided below.



## Process Outward NEFT- Customer Transfers via pain.001

When a NEFT customer transfer request is initiated through a pain.001 file, TPH will process the payment STP and generate the N.06 payment.

[Positive Workflow](#)

When processing a pain.001 as a bulk payment, once the payment is processed successfully to the 687 status, the DVD and CVD of all payments will be imposed to the date in the latest 972 SOD report using the DATE Api and the N.06 payment is generated.

The following will be the accounting entries for batch booking:

- DR. Customer Account.
- CR. Suspense Account.
- DR. Suspense Account (Individual Payment Instruction Amount).
- CR. Nostro Account (Individual Payment Instruction Amount).

1. Process the following pain.001 file.

   [](../../Resources/Images/India/PPINNP/NEFT-PAIN001-TPS0418-008-004-bulkpayments.xml)
2. The attached pain.001 file has two bulk and three transactions in total.


3. The first bulk has two transactions as per below.


4. The second bulk has one transaction as per below.


5. The file is processed in the bulk layer (BulkCTIInput).


6. The first bulk details are provided below.


7. The second bulk details are provided below.


8. As all the services are running, the payment details are provided below.
9. The first bulk transactions details are provided below.


10. The second bulk transactions details are provided below.


11. The first bulk transaction details for the parent transaction are provided below.


12. The `POR.TRANSACTION` details for the parent transaction is updated as per below.

    [](../../Resources/Images/India/PPINNP/POR TRANSACTION-BNK21105DBHBGHFB.pdf)
13. The posting lines details are provided below.


14. The accounting entries details are provided below.


15. As it was mentioned earlier, the first bulk consists of two transactions.
16. The details of the child transactions are provided below.


17. The audit trail details of the first child transaction are provided below.


18. The `POR.TRANSACTION` for the first child transaction is updated as per below.

    [](../../Resources/Images/India/PPINNP/POR TRANSACTION-BNK21105FMMFCKHD.pdf)
19. The posting lines details are provided below.


20. The accounting entries details are provided below.


21. The audit trail details of the second child transaction are provided below.


22. The `POR.TRANSACTION` for the second child transaction is updated as per below.

    [](../../Resources/Images/India/PPINNP/POR TRANSACTION4.pdf)
23. The posting lines details are provided below.


24. The accounting entries details are provided below.


25. The details of the second bulk transactions are provided below.


26. The audit trail of the parent transaction is provided below.


27. The `POR.TRANSACTION` for the parent transaction is updated as per below.

    [](../../Resources/Images/India/PPINNP/POR TRANSACTION5.pdf)
28. The posting lines details are provided below.


29. The accounting entries details are provided below.


30. The audit trail of the child transaction is provided below.


31. The `POR.TRANSACTION` for the child transaction is updated as per below.

    [](../../Resources/Images/India/PPINNP/POR TRANSACTION6.pdf)
32. The posting lines details are provided below.


33. The accounting entries details are provided below.


34. The generated outward files are provided below.

    [](../../Resources/Images/India/PPINNP/SOGEN21105000017.txt)

    [](../../Resources/Images/India/PPINNP/SOGEN21105000016.txt)

    [](../../Resources/Images/India/PPINNP/SOGEN21105000015.txt)

[Negative Workflow](#)

If a pain.001 is processed without beneficiary account number, then the payment is moved to the repair queue with the following error message: *Beneficiary Account Number is mandatory.*

1. Process the following pain.001 file.

   [](../../Resources/Images/India/PPINNP/NEFT-PAIN001-TPS010.xml)
2. The file is received and mapped in the received file.


3. Run the heavy service and the payment moves to the 235 status.


4. As the pain.001 is processed without a beneficiary account number, then the payment is moved to the repair queue with the following error message: *Beneficiary Account Number is mandatory.*



## Manage the Clearing Directory

The India NEFT clearing directory is the participant bank code directory that communicates which bank can be reached for India NEFT services of India clearing banks.

India clearing(RBI) distributes the participant directory file to all participants of the India NEFT clearing.

The `CA.CLEARING.DIRECTORY` application contains all the information from the India NEFT participant directory.

The information from the India NEFT participant directory can be uploaded by the bank user either manually or automatically.

Once the India NEFT participant directory content is successfully mapped to the `CA.CLEARING.DIRECTORY` application, any existing records in the clearing directory are left untouched by the upload (either manual or automatic).

[Upload the Participant Directory](#)

TPH provides the ability to accept the India NEFT participant directory and upload the participant information into the `CA.CLEARING.DIRECTORY` application using the INDCLRGClearingDirectory.uploadClrgDir Api. The bank user can add, delete and edit the uploaded information and during the deletion of IFSC the status will be marked as DISABLED.

The India NEFT participant directory is received as an XML file. The update date of the file will be the effective date (system date) for the participant banks that are listed in the clearing directory file. If an India NEFT participant directory with current or past date is uploaded, Temenos Transact will upload the records with the effective date (system date) as the next calendar date.

A IFSC clearing directory record has been created for NEFT.

[Automatic Upload](#)

The EB.CREATE.FILE.UPLOAD service allows the bank to automate the India NEFT participant directory file upload process:

- A text file, called information file, with a given name will be created in the folder (path) specified in the `EB.FILE.UPLOAD.PARAM` application. The text file will contain the name of the file that needs to be uploaded and the upload type.
- The service will read the text file and will identify which upload type should use, (in the above example INDCLRGDIR is a record in `EB.FILE.UPLOAD.TYPE` which indicates the folder where the India NEFT participant directory files will be copied) and will create the record in the `EB.FILE.UPLOAD` application.
- The T24.UPLOAD.PROCESS TSA.SERVICE will process the new `EB.FILE.UPLOAD` record and will upload the India NEFT participant directory file.

1. An xml file with the IFSC details and the payments.txt file is provided.

   [](../../Resources/Images/India/PPINNP/Files/payments.txt)

   [](../../Resources/Images/India/PPINNP/Files/AutomaticUpdate1.xml)


2. INDCLRGDIR folder has been creater in tcupload. Place the xml file in the INDCLRGDIR folder.
3. Place the payments.txt in the tcupload folder.


4. Run the BNK/EB.CREATE.FILE.UPLOAD service.The file will be upload in the `EB.FILE.UPLOAD` application.
5. Run the BNK/T24.UPLOAD.PROCESS service.
6. The record created in the `EB.FILE.UPLOAD` application will be updated with the *Service Status* as PROCESSED.


7. Two records will be created. One for NEFT and one for RTGS.


8. The NEFT record will be created with the *Status* as ENABLED.


9. The `CA.CLEARING.DIRECTORY.PARAM` record for NEFT is updated with the last upload date and the last effective date as the effective date. The *Last Source File Name* field is updated as the processed file’s name.



[Manual Upload](#)

A user can manually upload a file from a Temenos Transact directory by creating a record in the `EB.FILE.UPLOAD` application. To do this, the user can indicate the name of the file that will have to be uploaded and the type of the upload (`EB.FILE.UPLOAD.TYPE`).

Once the user creates the `EB.FILE.UPLOAD` record, the T24.UPLOAD.PROCESS service will process the request.

The T24.UPLOAD.PROCESS service is a generic file upload, and it will pick all the new file upload records created from the last time when the service ran.

If manual upload is done from old browser, upload path should be configured in tcserver.xml under C:\Temenos\jboss\standalone\deployments\tocfee.ear\tocfplugin-ra.rar\ :



The above configuration is not required if new browser is used.

1. An xml file with the IFSC details is provided.


2. Create a record in the `EB.FILE.UPLOAD` application and choose the *Upload Type* and file.


3. Validate, commit and authorise the record.


4. Run the BNK/T24.UPLOAD.PROCESS service.
5. The record created in the `EB.FILE.UPLOAD` application will be updated with the *Service Status* as PROCESSED.


6. Two records will be created, one for NEFT and one for RTGS.


7. The NEFT record is provided below.


8. The `CA.CLEARING.DIRECTORY.PARAM` record for NEFT is updated with the last upload date and the last effective date as the effective date. The *Last Source File Name* field is updated as the processed file’s name.

[Perform the Reachability Check from TPH](#)

TPH provides the ability to check reachability of India NEFT processing.

The reachability logic is provided below:

- The system will find the records in the clearing directory for the combination of IFSC and payment channel.
- The payment date is greater than or equal to the start date and effective date (system date) and lesser than or equal to the end date.
- Status is equal to ENABLED.
- If more than one record is found, the system will pick the record that has the most recent effective date (system date).

If a record is found, then the system will return an indicator that the IFSC is reachable. If a record is not found, then system will indicate that the IFSC is not reachable with an appropriate error code.

The reachability check is performed for returns also.

[Perform a Reachability Check when IFSC is Present in the Directory](#)

1. Ensure that an IFSC record exists in the `CLEARING.DIRECTORY` application with the *Status* as ENABLED.
2. Ensure that the effective date of clearing directory record is less than or equal to payment processing date.


3. Maintain a record in RD for the IFSC.


4. Initiate a PO for NEFT.


5. Run the medium weight service. It will move to the 235 status due to the non stp flow. Release the payment from repair queue.


6. Run the medium weight service and the payment will move to the 687 status.



[Perform a Reachability Check when IFSC is Not Present in the Directory](#)

1. Create a record for IFSC in the `RD.CENTRAL.BANK.DIR` application.
2. Ensure that there is no record for that IFSC in the clearing directory.


3. Initiate a PO for NEFT and an override will be displayed for reachability.


4. Accept and proceed. Run the medium weight service.


5. The payment goes to the 235 status with a reachability error.



[View the Clearing Directory Record Details](#)

1. The **Search Clearing Directory India** menu allows users to access the CLEARING.DIRECTORY.INDCLRGDIR.DETAILS enquiry to view the records from the `CA.CLEARING.DIRECTORY` application.


2. The CLEARING.DIRECTORY.INDCLRGDIR.DETAILS enquiry is displayed and the *IFSC Code* can be used as the search criteria.



In this topic

- [Working with NEFT Clearing](#WorkingwithNEFTClearing)

- [Assumptions and Exclusions](#AssumptionsandExclusions)
- [Initiate Outgoing Customer Transfers](#InitiateOutgoingCustomerTransfers)
- [Settlement Acknowledgment Messages](#SettlementAcknowledgmentMessages)
- [N03 Message from Clearing for Outward Payments](#N03MessagefromClearingforOutwardPayments)
- [Support of 972 Start of Day and N04 End of Day](#Supportof972StartofDayandN04EndofDay)
- [Beneficiary Bank Acknowledgment Messages](#BeneficiaryBankAcknowledgmentMessages)
- [Dates Calculation, Holiday and COB Check](#DatesCalculationHolidayandCOBCheck)
- [Inward Payments and Inward Return Payments](#InwardPaymentsandInwardReturnPayments)
- [Outward Returns](#OutwardReturns)
- [Process Outward NEFT- Customer Transfers via pain.001](#ProcessOutwardNEFTCustomerTransfersviapain001)
- [Manage the Clearing Directory](#ManagetheClearingDirectory)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:04:19 PM IST
# Introduction to NEFT Clearing - Mc Main Content

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/India/India/PPINNP/Introduction.htm#mc-main-content

---

# Introduction to NEFT Clearing

Updated On 08 November 2022 |
 3 Min(s) read

Feedback
Summarize

National Electronic Funds Transfer (NEFT) is an electronic funds transfer system maintained by the Reserve Bank of India (RBI). NEFT enables bank customers in India to transfer funds between any two NEFT enabled bank accounts on a one-to-one basis. It is done via electronic messages. A customer can initiate NEFT transfers 24/7 and are settled in half-hourly batches every day between 00:30 am and 00:00 am all through the year. There is no limit, either minimum or maximum, on the amount of funds that can be transferred using NEFT. The services can be broadly classified as below:

- NEFT outward credit transfers and returns.
- NEFT inward credit transfers and returns.

This module allows banks to process incoming and outgoing NEFT credit transfers, returns and the related messages.

The PAYMENT.ORDER,INDNEFT.INPUT version is introduced as part of this functionality to allow users to initiate NEFT payment transfers.

This functionality also allows banks to process the outward N07 file generation, process manual and automatic returns and support the receipt of ADMI messages.

For an inward credit transfer, if there is an issue with the credit account, TPH will automatically return the inward CT by generating an N07 message and the payment will move to status ‘687’. The original transaction will be reversed. Positive and negative ADMI messages are received for N07.

## Clearing Directory Upload

This functionality provides banks with the ability to upload the participant directory for India NEFT processing service and to check the reachability for the participants from TPH.

The India NEFT participant directory has been implemented in TPHusing the standard Temenos Transact file upload framework that is currently employed for the other clearing directories.

This has been achieved by configuring the Temenos Transact application and the India NEFT participant directory specific loading API which will fetch the values from xml file and upload them in the NEFT clearing directories for the given Indian Financial System Code (IFSC).
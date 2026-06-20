# Working with MASAV Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Israel/Israel/MASAV_PPMASV/Working_with.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Israel > [MASAV](../../Israel/MASAV_PPMASV/Introduction.htm) > Working with

- Israel;)
  - [MASAV MASAV](../../Israel/MASAV_PPMASV/Introduction.htm)
    - [Introduction](../../Israel/MASAV_PPMASV/Introduction.htm)
    - [Configuration](../../Israel/MASAV_PPMASV/Configuration.htm)
    - [Working with](../../Israel/MASAV_PPMASV/Working_with.htm)
    - [Tasks](../../Israel/MASAV_PPMASV/Tasks.htm)
    - [Outputs](../../Israel/MASAV_PPMASV/Outputs.htm)

Payments

# Working with MASAV Clearing

Updated On 06 July 2023 |
 3 Min(s) read

Feedback
Summarize

This section helps the user to understand the working of MASAV clearing payments.

## Processing Credit Transfer Request

The user needs to perform the following actions:

1. Initiate the MASAV credit transfer from Payment Order by using the MASAVCTI version.

/Working with MASAV Clearing.png)


/Working with MASAV Clearing_1.png)

2. Enter the required details in the following field:

- *Debit Account*
- *Ordering Reference*
- *Instruction ID Reference*
- *End to End Reference*
- *Beneficiary ID*
- *Beneficiary Account No* (*Account number*)
- *Beneficiary OT ID* (*Customer ID number*)
- *Beneficiary Name* (*Customer name*)
- *Debit Value Date*
- *Payment Currency*
- *Payment Amount*
- *Ordering OT ID* (*Institution ID*)
- *Ordering OT ID Type = Private*
- *Execution Date* (*Charging date*)
- *Ordering Cust Name* (*Institution name*)
- *Acct with Bank Clearing Code* ( concatenates and stores the *Bank ID* and *Branch* Number)

After authorisation, the payment order request is placed in TPH for further processing.

/Working with MASAV Clearing_2.png)

TPH processes the payment successfully and performs posting.

/Working with MASAV Clearing_3.png)

The below screenshot displays the outward file generated to MASAV.

/Working with MASAV Clearing_4.png)

[Handling Inward Credit Transfer Returns](#)

On receiving an incoming return payment message, the solutions are moved to repair (as configured in product determination). When the incoming return transaction is processed from repair, the original payment is rejected and the status changes to ‘Payment Completed with Return’.

/Working with MASAV Clearing_5.png)


/Working with MASAV Clearing_6.png)


/Working with MASAV Clearing_7.png)

## Sending DD to MASAV Clearing

The user can initiate an outward direct debit initiation request through Temenos Transact DD module.

/Working with MASAV Clearing_8.png)

After Close of Business (COB), the payment is moved to the payment system.

/Working with MASAV Clearing_9.png)

After mapping, the payment is processed in the payment system.

/Working with MASAV Clearing_10.png)


/Working with MASAV Clearing_11.png)

[Processing Inward Direct Debit Returns](#)

On receiving incoming return payment message, it rejects and moves the original payment to ‘Payment Completed with Return’ status. This happens when the return payment is processed till its final status is ‘Complete’.

- Check whether the return payment is received and mapped to POR.TRANSACTION table.

/Working with MASAV Clearing_12.png)


/Working with MASAV Clearing_13.png)


/Working with MASAV Clearing_14.png)

In this topic

- [Working with MASAV Clearing](#WorkingwithMASAVClearing)

- [Processing Credit Transfer Request](#ProcessingCreditTransferRequest)
- [Sending DD to MASAV Clearing](#SendingDDtoMASAVClearing)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:26:18 PM IST
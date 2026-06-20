# Configuring Saudi Arabian Riyal Interbank Express (SARIE) - Reachability In Sarie

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/SaudiArabia/SaudiArabia/Saudi_PPSARI/Configuration.htm#Reachability_in_SARIE

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Saudi Arabia > [Saudi Arabia Riyal Interbank Express (SARIE)](../../SaudiArabia/Saudi_PPSARI/Introduction.htm) > Configuration

- Saudi Arabia;)
  - [Saudi Arabia Riyal Interbank Express (SARIE) Saudi Arabia Riyal Interbank Express (SARIE)](../../SaudiArabia/Saudi_PPSARI/Introduction.htm)
    - [Introduction](../../SaudiArabia/Saudi_PPSARI/Introduction.htm)
    - [Configuration](../../SaudiArabia/Saudi_PPSARI/Configuration.htm)
    - [Working with](../../SaudiArabia/Saudi_PPSARI/Working_with.htm)
    - [Tasks](../../SaudiArabia/Saudi_PPSARI/Tasks.htm)
    - [Outputs](../../SaudiArabia/Saudi_PPSARI/Outputs.htm)
  - [Saudi Arabia Instant Payments System (SAIPS) Saudi Arabia Instant Payments System (SAIPS)](../../SaudiArabia/Saudi_Instant_Payments_System_PPISIP/Introduction.htm)

Payments

# Configuring Saudi Arabian Riyal Interbank Express (SARIE)

Updated On 06 October 2022 |
 4 Min(s) read

Feedback
Summarize

This section helps the user to configure Payment Order Product, reachability, clearing attributes, clearing cut-off, account number, currency, and future-dated payment.

## Payment Order Product

To configure the Payment Order Product, perform the following:

1. Go to **Admin Menu**>**Payments Hub**>**Payment Order Admin Menu**>**Payment Order Product Setup**.
2. Enter the required details in the following fields in `PAYMENT.ORDER.PRODUCT` table with version name SARIE.CTR.INPUT:

| Field | Value | Description |
| --- | --- | --- |
| *ID* | SARIE | Product name in `PO` application |
| *Pay Through Beneficiary* | Yes | Creditor participant acts as intermediary and the ultimate beneficiary is different |
| *Allow Future Date* | 14C | Number of days for the future value date |
| *Allow IBAN* | Yes | Allows International Bank Account Number (IBAN) |
| *Allow BIC* | Yes | Allows the Bank Identifier Code (BIC) |
| *Allow FX* | Yes | Have different debit account and credit account currency other than transferred currency SAR |
| *Reachability Check* | BIC | Performs the check based on BIC |
| *Clearing Channel* | SARIE | Channel that is used for clearing |



## Reachability in SARIE

To configure reachability key fields, perform the following:

1. Go to **Admin Menu**>**Framework Parameter**>**Clearing Directory**>**Clearing Directory Parameter**.
2. Configure the *Reachability Key* fields with BIC and payment channel in `CA.CLEARING.DIRECTORY.PARAM` table.



3. To configure the participant bank details, go to **Admin Menu**>**Framework Parameter**>**Clearing Directory**
4. Enter the required details in the following fields in `CA.CLEARING.DIRECTORY` table.

| Field | Value | Description |
| --- | --- | --- |
| *Payment Channel* | SARIE | Holds the clearing channel through which the beneficiary institution is reachable |
| *BIC* | ARNBSARI | Bank Identifier Code (BIC) of the participant |
| *Reachability Type* | D | Participant bank is a direct (D) or indirect (I) participant |



## Clearing Attributes

To define clearing specific attributes, perform the following:

1. Go to **Admin Menu**>**Payments**>**Payments Hub**>**Local Clearing**>**Clearing**.
2. Enter the required details in the following fields `PP.CLEARING` table.

| Field | Value | Description |
| --- | --- | --- |
| *Clearing Currency* | SAR | Currency used in clearing |
| *Clearing Country Code* | SA | Country code for the clearing |
| *RTGS System* | Y | Indicates that clearing is RTGS |
| *File Transfer Indicator* | N | Clearing is transaction based |
| *Skip Reachability* | N | Does not skip the reachability check |
| *Settlement Type* | Gross | Type of settlement used in clearing |



## Clearing Cut-Off Time

To configure cut-off time, perform the following:

1. Go to **Admin Menu**>**Payments Hub**>**Routing & Settlement**>**Channel Cut-Off**.
2. Enter the required details in the following fields in `PP.CHANNEL.CUTOFF` table.

| Field | Value | Description |
| --- | --- | --- |
| *Cutoff Time* | 16:00 | Time after which the channel cannot be used for routing payments on a given day. |
| *Cutoff Shift* | 0 | Number of cut-off shift days used to determine the next processing date, when a payment can be routed through the channel defined. |



## Clearing Account Number and Currency

To configure clearing account number and currency code, perform the following:

1. Go to **Admin Menu**>**Payment Hub**>**Local Clearing**>**Clearing Setting**.
2. Enter the required details in the following fields in `PP.CLEARING.SETTING` table:

| Field | Value | Description |
| --- | --- | --- |
| *ID* | SARIE.SAR.S.SARIECT.CT | Unique identifier of transaction. It uses the following format: Clearing Name<.>Currency<.>Sent or Received<.>Clearing Transaction Type |
| *Clearing Account Number* | 18716 | Nostro account number of the clearing in the clearing currency |



## Future Dated Payment

On receiving an incoming payment with future value date, the system processes the payment on the date of receipt from clearing.

The credit value date needs to be given in the exposure date.

To configure a future dated payment, perform the following:

1. Go to **Admin Menu**>**Payments**>**Payment Hub**>**Bank Condition**.
2. In `PP.BANK.CONDITIONS` table, set *Warehouse Flag* as N.



3. Go to **Admin Menu**>**Payment Hub**>**Date Determination**>**Exposure Date**.
4. In `PP.EXPOSURE.DATE` table, set *Exposure Date Flag* as CVD.



In this topic

- [Configuring Saudi Arabian Riyal Interbank Express (SARIE)](#ConfiguringSaudiArabianRiyalInterbankExpressSARIE)

- [Payment Order Product](#PaymentOrderProduct)
- [Reachability in SARIE](#ReachabilityinSARIE)
- [Clearing Attributes](#ClearingAttributes)
- [Clearing Cut-Off Time](#ClearingCutOffTime)
- [Clearing Account Number and Currency](#ClearingAccountNumberandCurrency)
- [Future Dated Payment](#FutureDatedPayment)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:21:37 PM IST
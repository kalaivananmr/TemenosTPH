# Configuring MASAV Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Israel/Israel/MASAV_PPMASV/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Israel > [MASAV](../../Israel/MASAV_PPMASV/Introduction.htm) > Configuration

- Israel;)
  - [MASAV MASAV](../../Israel/MASAV_PPMASV/Introduction.htm)
    - [Introduction](../../Israel/MASAV_PPMASV/Introduction.htm)
    - [Configuration](../../Israel/MASAV_PPMASV/Configuration.htm)
    - [Working with](../../Israel/MASAV_PPMASV/Working_with.htm)
    - [Tasks](../../Israel/MASAV_PPMASV/Tasks.htm)
    - [Outputs](../../Israel/MASAV_PPMASV/Outputs.htm)

Payments

# Configuring MASAV Clearing

Updated On 06 July 2023 |
 2 Min(s) read

Feedback
Summarize

This section describes the configuration options the system offers in MASAV.

1. To configure MASAV, go to **Admin Menu**>**Payments Hub**>**Local Clearing**>**Clearing**. An example of the configuration is shown below.

/Configuring MASAV Clearing.png)


/Configuring MASAV Clearing_1.png)

2. Enter the required details in the following fields:

| Field | Description |
| --- | --- |
| *Outgoing Message Type* | Defines the message types supported by MASAV |
| *Settlement Type* | Set to NET as MASAV is a net settlement system  This can be skipped as the Settlement System Type is only applicable for transaction-based clearings (configured as *Clearingfiletransactionind* = T) |

3. To define the additional characteristics of payment based on the direction, go to **Admin Menu**>**Payments Hub**>**Local Clearing**>**Clearing Setting**.

/Configuring MASAV Clearing_2.png)

4. Enter the required details in the following fields:

| Field | Description |
| --- | --- |
| *Message Direction* | Direction of the payment for which clearing setting record is created |
| *Clearing Account Number* | Clearing account (Nostro account) in clearing currency |
| *Message Payment Type* | Type of message for which the clearing setting record is created |

/Configuring MASAV Clearing_3.png)

## Configuring Clearing Cut-Off

The user needs to perform the following:

1. To configure different cut-off times, go to **Routing & Settlement**>**Channel Cut-off**.

/Configuring MASAV Clearing_4.png)

2. Select the *ASAPALAP* (output parameter) radio button as ASAP in the CHANNEL.CUTOFF table for source MASAV and respective message type.

In this topic

- [Configuring MASAV Clearing](#ConfiguringMASAVClearing)

- [Configuring Clearing Cut-Off](#ConfiguringClearingCutOff)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:26:18 PM IST
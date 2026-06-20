# Temenos Transact Services

> Source: https://docs.temenos.com/docs/Solutions/T24_Transact/Framework/ST/Services/Misc/Services.htm

---

2. [Temenos Transact](../../../../content/T24_Transact.html)

- System Tables;)

Temenos Transact

# Temenos Transact Services

Updated On 10 July 2024 |  64 Min(s) read

Feedback
Summarize

## Accounting Unit (AU)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | AU.INTERNAL.ACCOUNT.CLOSURE | Closes internal accounts in accounting companies | AU.INTERNAL.ACCOUNT.CLOSURE | FIN |



## Accounts (AC)

| S.No | Job Name | Description of Job | Batch Name | Classification |
| --- | --- | --- | --- | --- |
| 1 | AC.ACCOUNTING.SERVICE | Maintains the unauthenticated entries at account level based on the AC.UNAUTH.ENTRY or AC.FWD.UNAU.ENTRY file | AC.ACCOUNTING.SERVICE | FIN |
| 2 | AC.CUS.BALANCE.REPORTING.TAKEON | Loads the historical account statement data to read only database for customer reporting enquiries using component service | AC.CUS.BALANCE.REPORTING.TAKEON | FIN |
| 3 | AC.HVT.MERGE.SERVICE | Merges the trigger records and update the corresponding account related tables | AC.HVT.MERGE.SERVICE | FIN |
| 4 | AC.INTEG.CAL.CHECK.SERVICE | Processes the AC.INTEGRITY.CAL.DATA record using check routines attached in the batch record and deletes the same after procesing | AC.INTEG.CAL.CHECK.SERVICE | FIN |
| 5 | AC.INTEG.PURGE.CAL.SERVICE | Deletes the list of AC.INTEG.CAL.SUMMARY records dated within the period defined in the batch details of the service | AC.INTEG.PURGE.CAL.SERVICE | FIN |
| 6 | AC.INTEGRITY.CHECK.SERVICE | Processes the AC.INTEGRITY.ACCOUNTING record using check routines attached in the batch record and deletes the same after procesing | AC.INTEGRITY.CHECK.SERVICE | FIN |
| 7 | AC.LOCKED.EVENTS.TAKEON | Exposes the existing locked events table to Data Framework related tables | AC.LOCKED.EVENTS.TAKEON | FIN |
| 8 | AC.NSF.REVALUATION.SERVICE | Revaluates the NSF charges posted for back value dated credit entry | AC.NSF.REVALUATION.SERVICE | FIN |
| 9 | AC.PROCESS.ENTRY.EVENT.SERVICE | Determine the exit points and triggers IF points to stream data to data events table | AC.PROCESS.ENTRY.EVENT.SERVICE | FIN |
| 10 | AC.PROCESS.TRANS.DATA | Processes AC.TRANS.DATA with respect to Trans data subscription | AC.PROCESS.TRANS.DATA | FIN |
| 11 | AC.STMT.DELIVERY.SERVICE | Picks the details from service detail workfile or handoff and generates the delivery messages | AC.STMT.DELIVERY.SERVICE | FIN |
| 12 | AC.UPDATE.LOCKED.SERVICE | Service routine to reinstate the limit amount based on the account locked amount attached to it with respect to setup in ACCOUNT.PARAMETER | AC.UPDATE.LOCKED.SERVICE | FIN |
| 13 | CHEQUE.PROCESS | Updates the cheque batch correctly on verifying the CHEQUE.CHANGE record | CHEQUE.PROCESS | FIN |
| 14 | AC.UPDATE.LOCKED.SERVICE | Service routine that reinstates the limit amount based on the account locked amount attached to it with respect to setup in ACCOUNT.PARAMETER | AC.UPDATE.LOCKED.SERVICE | CUS |

## All in One (AZ)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | AZ.PROCESS.CC.SCH | Calculate the principal (CC) amounts for credit cards on BILL.CLOSE .Selection File:CARD.BILL.CLOSE.DATE. Control list: Banks current date to next working day | AIO.ACC.EOD | FIN |
| 2 | AZ.PROCESS.CI.SCH | Calculates interest(CI) for the next repayment date in credit cards on the repayment date. Selection File:CARD.REPAYMENT.DATE. Control list: After last working day to bank's current date | AIO.ACC.EOD | FIN |
| 3 | AZ.PRE.PROCESS.SCH | Processes rate changes for contracts linked to Basic Interest key and also disbursements of loans . Selection File: AZ.ACCOUNT | AIO.ACC.EOD | FIN |
| 4 | AZ.PRE.PROCESS.SCH | Processes rate changes for contracts linked to Basic Interest key and also disbursements of loans . Selection File: AZ.ACCOUNT | AIO.ACC.SOD | FIN |
| 5 | AZ.FIND.LATE.PAYMENT.SOD | Finds the deferred payment for Savings plan deposits during Split month end .Selection file:AZ.DEPOSIT.LIST. Control list: From 1st of Month to Last calender day prior to Bank's current date | AIO.ACC.SOD | FIN |
| 6 | AZ.PURGE.TELLER.DEFAULT | Purges TELLER.DEFAULT records created for AZ contract and are used in Teller transactions. Selection file: TELLER.DEFAULT | AIO.ACC.EOD | FIN |
| 7 | AZ.POST.PROCESS.SCH | Processes Delivery limit updation and cycling of 'R' schedules for AZ loans at end of day and cycling of 'R' schedules during Start of day. Selection File: AZ.ACCOUNT. | AIO.ACC.EOD | FIN |
| 8 | AZ.POST.PROCESS.SCH | Processes Delivery limit updation and cycling of 'R' schedules for AZ loans at end of day and cycling of 'R' schedules during Start of day. Selection File: AZ.ACCOUNT. | AIO.ACC.SOD | FIN |
| 9 | AZ.CARD.PD.EOD | Creates PD record for AZ Credit Card on repayment date Selection file: CARD.REPAYMENT.DATE Control list:After last working day to current Bank date | AIO.ACC.EOD | FIN |
| 10 | AZ.SOD.PROCESS.SCH | Processes Schedules PBCIN and A for AZ contracts during split month end . Selection file: AZ.SCHEDULES or AZ.REPAY.ACCOUNT (COB.ASP is flagged ). Control list: First day of month to last calender day prior to Period end | AIO.ACC.SOD | FIN |
| 11 | AZ.FIND.LATE.PAYMENT | Finds the deferred payment for Savings plan deposits .Selection file: AZ.DEPOSIT.LIST. Control list: Bank's current date to Period end | AIO.ACC.EOD | FIN |
| 12 | AZ.PURGE.LIST.FILES | Purges processed internal list files. Selection file :AZ.DEPOSIT.LISTAZ.INTEREST.WORK. | AIO.ACC.SOD | FIN |
| 13 | AZ.PROCESS.MATURITY | Maturity schedule processing for AZ loans and deposits during Start of day. Selection file: AZ.ACCOUNT | AIO.ACC.SOD | FIN |
| 14 | AZ.EOD.PROCESS.SCH | Processes Schedules PBCIN and A for AZ contracts. Selection file:AZ.SCHEDULES or AZ.REPAY.ACCOUNT (COB.ASP is flagged ). Control list: Current Bank's date to Period end | AIO.ACC.EOD | FIN |
| 15 | AZ.UNAUTH.PROCESSING | Job handles AZ generic unauth processing for deleting the AZ record and related applications FT/TELLER linked to AZ contracts. Selection file: AZ.ACCOUNT.WORK AZ.ACCOUNT$NAU. | AIO.ACC.EOD | FIN |
| 16 | AZ.COLLECT.PENAL.CHARGES | Collect penalty charges which are due to be collected today for Savings plan. Selection file: AZ.ACCT.BAL. Control list:Last working day to current bank date | AIO.ACC.EOD | FIN |

## Arrangement Architecture (AA)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | AA.AGENT.COMMISSION.SERVICE | Processes agent commission | BNK/AA.AGENT.COMMISSION.SERVICE | FIN |
| 2 | AA.AGENT.SERVICE.PROCESS | Hands over request to process commission to AA.AGENT.COMMISSION.SERVICE | BNK/AA.EOD.PROCESS | FIN |
| BNK/AA.INTRADAY.PROCESS | FIN |
| 3 | AA.ARCHIVE.SERVICE | Moves activity history, bill details and account details to corresponding .HIST tables based on threshold and retains values defined in AA.PARAMETER | BNK/AA.ARCHIVE.SERVICE | FIN |
| 4 | AA.ARR.PRODUCT.TRACKER | Tracks product changes and applies the corresponding change to existing arrangements if the corresponding property is set for tracking | BNK/AA.ARR.PRODUCT.TRACKER | FIN |
| BNK/AA.EOD.PROCESS | FIN |
| 5 | AA.ARR.TRACKER.SERVICE | Tracks the changes done in the parent and applies in inherited arrangement, if an arrangement is inherited from another arrangement | BNK/AA.ARR.TRACKER.SERVICE | FIN |
| BNK/AA.EOD.PROCESS | FIN |
| 6 | AA.CHARGE.HANDOFF.PROCESS | Processes the non-financial arrangement charge handoff to financial arrangement (Billing and Accounting) side based on the charge details stored in the AA.CHARGE.HANDOFF.DETAILS file | BNK/AA.CHARGE.HANDOFF.PROCESS | FIN |
| 7 | AA.COB.PAY.IN.OUT | Processes all non-bulk mode AA payments made in end of day | BNK/AA.EOD.PROCESS | FIN |
| BNK/AA.INTRADAY.PROCESS | FIN |
| BNK/AA.SOD.PROCESS | FIN |
| 8 | AA.COLLECT.CHARGE.PROCESS | Processes charge based on non-sufficient fund configuration | BNK/AA.COLLECT.CHARGE.PROCESS | FIN |
| 9 | AA.CRA.SERVICE | Fetches the arrangement for which redundant relation codes have to be removed | BNK/AA.CRA.SERVICE | FIN |
| BNK/AA.EOD.PROCESS | FIN |
| 10 | AA.CRA.STATIC.SERVICE | Removes CRA customer whose relation codes are removed in CUSTOMER application | BNK/AA.EOD.PROCESS | FIN |
| 11 | AA.CREATE.NAU.ACTIVITIES | Captures the AAA that were deleted during AA.DELETE.NAU.ACTIVITIES | BNK/AA.INTRADAY.PROCESS | FIN |
| BNK/AA.SOD.PROCESS | FIN |
| 12 | AA.DELETE.NAU.ACTIVITIES | AAA that are in INAU are deleted and handed over to the SOD JOB AA.CREATE.NAU.ACTIVITIES to post back again | BNK/AA.EOD.PROCESS | FIN |
| BNK/AA.INTRADAY.PROCESS | FIN |
| 13 | AA.FINAL.SERVICE.PROCESS | Proccess the arrangements that belong to agent and rewards | BNK/AA.EOD.PROCESS | FIN |
| BNK/AA.INTRADAY.PROCESS | FIN |
| BNK/AA.SOD.PROCESS | FIN |
| 14 | AA.HOLIDAY.SERVICE | Reschedules the scheduled activities when holiday table is amended to define holiday | BNK/AA.HOLIDAY.SERVICE | FIN |
| 15 | AA.INTEGRITY.CAPTURE.SERVICE | Induces bug in test contracts by modifying the values using AA.INTEGRITY.CAPTURE template to test that the integrity tool that reports all problematic contracts in AA.INTEGRITY.REPORT   Note: This service strictly cannot be used in production environments. | BNK/AA.INTEGRITY.CAPTURE.SERVICE | FIN |
| 16 | AA.INTEGRITY.CHECK | Checks every arrangement by comparing various tables against the balances and reports problematic arrangements | BNK/AA.INTEGRITY.CHECK | FIN |
| BNK/AA.SYSTEM.CHECKS | FIN |
| 17 | AA.LIMIT.ACCOUNT.PROCESS | Handles processing of all scheduled activities for Arrangements of  Limit Account type | BNK/AA.SYSTEM.END.OF.DAY | FIN |
| 18 | AA.ONLINE.PAY.IN.OUT | Processes all non-bulk mode online AA payments | BNK/AA.ONLINE.PAY.IN.OUT | FIN |
| 19 | AA.ONLINE.SERVICE | Processes online accruals and capitailisation so as to reduce cob timing based on setup in AA.ACCRUAL.FREQUENCY for accruals and payment schedule condition for capitalisation | BNK/AA.ONLINE.SERVICE | FIN |
| 20 | AA.PROCESS.ACTIVITIES | Triggers Arrangement Activity from non-AA applications | BNK/AA.PROCESS.ACTIVITIES | FIN |
| 21 | AA.PROCESS.LEVEL.ARRANGEMENTS | Processes Arrangements that are interlinked during COB | BNK/AA.EOD.PROCESS | FIN |
| BNK/AA.INTRADAY.PROCESS | FIN |
| BNK/AA.SOD.PROCESS | FIN |
| 22 | AA.PROCESS.POSTING.RESTRICTION | Updates or removes posting restriction from base account, based on posting restriction start and end date defined in ACCOUNT arrangement condition | BNK/AA.PROCESS.POSTING.RESTRICTION | FIN |
| 23 | AA.PRODUCT.CREATION.SERVICE | Creates products from EB.PRODUCT.IMPORTER definition for EPD | BNK/AA.PRODUCT.CREATION.SERVICE | FIN |
| 24 | AA.PRODUCT.IMPORT.SERVICE | Creates imported product defined using Product Import Manager | BNK/AA.PRODUCT.IMPORT.SERVICE | FIN |
| 25 | AA.PUBLISH.SERVICE | Performs proof and publish of AA products | BNK/AA.PUBLISH.SERVICE | FIN |
| 26 | AA.RR.PROCESS | Performs offline reverse and replay processing for Accounts product line as part of End Of Day process | BNK/AA.EOD.PROCESS | FIN |
| 27 | AA.RR.SERVICE | Responsible for Offline reverse and replay processing for Accounts product line | BNK/AA.RR.SERVICE | FIN |
| 28 | AA.SERVICE.PROCESS | Processes for all AA scheduled activities | BNK/AA.EOD.PROCESS | FIN |
| BNK/AA.INTRADAY.PROCESS | FIN |
| BNK/AA.SOD.PROCESS | FIN |
| 29 | AA.SIMULATION.SERVICE | Simulates or executes the AAA activities which are captured through AA.SIMULATION.CAPTURE | BNK/AA.SIMULATION.SERVICE | FIN |
| 30 | AA.SYSTEM.END.OF.DAY | Processes the activities that are triggered from external application, which are not scheduled activities | BNK/AA.EOD.PROCESS | FIN |
| BNK/AA.INTRADAY.PROCESS | FIN |
| BNK/AA.SOD.PROCESS | FIN |
| BNK/AA.SYSTEM.END.OF.DAY | FIN |
| 31 | AA.UNAUTH.ACTIVITIES.CHECK | Checks for NAU activities that are not recreated after SOD | BNK/AA.INTEGRITY.CHECK | FIN |
| 32 | AA.UPDATE.AGENT.CUSTOMER.LIST | Updates AA.AGENT.CUSTOMER.LIST | BNK/AA.UPDATE.AGENT.CUSTOMER.LIST | FIN |



## Cheque & Draft Issue Management (CQ)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | CARD.BILL.CLOSE.REPAY.DATES | Converts card bill close and repay dates correctly | CARD.BILL.CLOSE.REPAY.DATES | FIN |
| 2 | DELETE.CLOSED.ACCOUNT.CHEQUES | Moves CHEQUE.ISSUE and its concat to HIS irrespective of cheque status and deletes the live and NAU records | DELETE.CLOSED.ACCOUNT.CHEQUES | FIN |

## Centralised Reference Data (RD)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | RD.UPDATE.LEI.CONCAT.TAKEON | One time service that updates RD.LEI.CONCAT file for the existing RD.CENTRAL.BANK.DIR records | RD.UPDATE.LEI.CONCAT.TAKEON | INT |
| 2 | RD.DELETE.BANK.DIR | Reverses the RD.CENTRAL.BANK.DIR in DELETE status | RD.DELETE.BANK.DIR | INT |
| 3 | RD.GPI.DELETE.SERVICE | Reverses the RD.SWIFT.GPI.DIR inDELETE status | RD.GPI.DELETE.SERVICE | INT |
| 4 | RD.GPI.MERGE.FUTURE.SERVICE | Merges future dated RD.SWIFT.GPI.DIR records | RD.GPI.MERGE.FUTURE.SERVICE | INT |
| 5 | RD.MERGE.FUT.BANK.DIR | Merges future dated RD.CENTRAL.BANK.DIR records | RD.MERGE.FUT.BANK.DIR | INT |
| 6 | RD.UPLOAD.BANK.DIR.SERVICE | Uploads bank directory plus records in RD.CENTRAL.BANK.DIR file | RD.UPLOAD.BANK.DIR.SERVICE | INT |

## Collateral Management (CO,CX)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | CO.CALC.CUST.COLL.SERVICE | Calculates collateral deficit or excess based on the collateral valuation parameter | CO.CALC.CUST.COLL.SERVICE | CUS |
| 2 | CO.EXCLUDE.SERVICE | Adds or removes the exclusion ID from the collateral, upon creation or reversal of COLLATERAL.EXCLUSION | CO.EXCLUDE.SERVICE | CUS |
| 3 | CO.RECALC.CUST.COLL | Calculates customer deficit based on the Collateral Valuation parameter | CO.RECALC.CUST.COLL | CUS |
| 4 | CO.RECALC.SUFFICIENCY.RATIO | Recalculates the sufficiency ratio for the Collateral Pool | CO.RECALC.SUFFICIENCY.RATIO | CUS |
| 5 | CO.REPORT.EXCEPTIONS | Processes exceptions  of COLLATERAL.POOL and COLLATERAL.ACCOUNT based on the exceptions trigger file | CO.REPORT.EXCEPTIONS | CUS |
| 6 | COLLATERAL.ONLINE.REVALUATION | Performs the online collateral revaluation.  Note: The limit and collateral right are processed only when online update is set to yes in limit and collateral type respectively | COLLATERAL.ONLINE.REVALUATION | CUS |
| 7 | CO.REBUILD.ALLOC.PRIORITY | Updates the LIMIT.COL.ALLOC.WORK and COLLATERAL.RIGHT based on the reallocation rule set in the CO.REALLOCATION.PARAMETER | CO.REBUILD.ALLOC.PRIORITY | FIN |

## Collections (CL)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | CL.PROCESS.COLLECTION |  | CL.COB.PROCESS | CUS |
| 2 | CL.COLL.INCENTIVE.CALC |  | CL.COB.PROCESS | CUS |
| 3 | CL.CALC.AGENCY.COMM |  | CL.COB.PROCESS | CUS |

## Confirmation Matching (CM)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | CM.FIND.MATCH.MESSAGE | Controls the process of automated comfirmation matching | CM.FIND.MATCH.MESSAGE | INT |
| 2 | CM.NEW.MESSAGE | Updates CM.MATCH.ITEM and CM.MESSAGAE | CM.NEW.MESSAGE | INT |

## Contact Preferences (PF)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | DE.UPD.PRD.DCP.TAKEON | One time service that updates DE.PRODUCT from DE.CUSTOMER.PREFERENCES | DE.UPD.PRD.DCP.TAKEON | INT |
| 2 | HOLD.MAIL.PRD.ONLINE | Processes HOLD MAILS | HOLD.MAIL.PRD.ONLINE | INT |

## Currency Redenomination (EU)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | EU.ARCHIVED.ACCT.CONVERSION | Processes each records in EU.CONVERSION.PARAM | EU.ARCHIVED.ACCT.CONVERSION | FIN |

## Customer & Account Balance Reporting Model (DA)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | DA.ACCT.ACTIV.TAKEON | Performs initial data takeon for all Acct activity balances for DF customer.  Note: Balance Reporting model runs only once. | DA.ACCT.ACTIV.TAKEON | FIN |
| 2 | DA.STMT.ENT.TAKEON | Performs initial takeon of stmt entry data for Customer Balance Reporting model.  Note: It should be run only once | DA.STMT.ENT.TAKEON | FIN |

## Delivery (DE)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | DE.EOP.INWARD | Performs End of Period processing for inward messages | DE.EOP.INWARD | FIN |
| 2 | DE.EOP.OUTWARD | Performs End of Period processing for outward messages | DE.EOP.OUTWARD | FIN |
| 3 | EBQA.ARCHIVE | Archives EB.QUERIES.AND.ANSWERS | EBQA.ARCHIVE | FIN |
| 4 | EBQA.UPD.CREATE.DATE | Updates CREATION.DATE in old EBQA records | EBQA.UPD.CREATE.DATE | FIN |
| 5 | ISOMX.IN | Processes inward messages arrived through generic interface using respective formatting routine | ISOMX.IN | FIN |
| 6 | DE.DISP.TIMECHECK | Emulates the functionality of DE.MM.TIMECHECK | DE.HOLD.KEY.RELEASE | FIN |
| 7 | DE.PRINT | Prints the delivery advice | DE.PRINT | FIN |
| 8 | EMAIL.OUT | Formats the messages in respective carrier, also sends the formatted message to the interface, if any | DE FORMATTING SERVICE | FIN |
| 9 | ISOMX.OUT | Updates transformed message in delivery files | ISOMX.OUT | FIN |
| 10 | SECUREMSG.OUT | Formats the messages in respective carrier and also sends the formatted message to the interface, if any | SECUREMSG.OUT | FIN |
| 11 | SMS.OUT | Formats the messages in respective carrier and also sends the formatted message to the interface, if any | DE FORMATTING SERVICE | FIN |
| 12 | TEMPLATE.SPOOL | Writes the message contents to the printer server queue. It is then accessed by the GUI print server, which invokes WORD to print the message. | TEMPLATE.SPOOL | FIN |
| 13 | XML.OUT | Formats the messages in respective carrier and also sends the formatted message to the interface, if any | XML.OUT | FIN |

## Derivatives (DX)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | DX.SOD.RP.REBUILD | This process maintains the value dated positions in DX.REP.POSITION | DX.START.OF.DAY | FIN |
| 2 | DX.COB.FUNDS.BLOCK | To block available funds | DX.END.OF.DAY | FIN |
| 3 | DX.COB.WORKFILE.TIDY | To archive DX.COB.WORKFILE when COUNTDOWN reached 0 | DX.END.OF.DAY | FIN |
| 4 | DX.STATIC.CHANGES | CRF Static change update for Derivatives | DX.END.OF.DAY | FIN |
| 5 | DX.CRF.HIST.CREATE | CRF History create update for Derivatives | DX.END.OF.DAY | FIN |
| 6 | DX.REBUILD.CONTRACT.DATES | Rebuild DX.CONTRACT.DATES | DX.END.OF.DAY | FIN |
| 7 | DX.COB.CLEAR.HISTORY | Clears DX.COB.WORKFILE.HISTORY based on the days specified in HLD.WORK.HIST.DAYS of DX.PARAMETER | DX.END.OF.DAY | FIN |
| 8 | DX.CONV.PM.POSITIONS | To convert the existing PTA and Position class records captured from derivatives module | DX.CONV.PM.POSITIONS | FIN |
| 9 | DX.CLEAR.CONTRACT.DATES | Clears DX.CONTRACT.DATES | DX.END.OF.DAY | FIN |
| 10 | DX.COB.CLEAR.MKT.HIST | Deletes DX.MARKET.PRICE.HISTORY record when the date found in history record key is less than the calculated working date based on the PRICE.DAYS provided in DX.PARAMETER record | DX.END.OF.DAY | FIN |
| 11 | DX.COB.REVALUE | Selects DX.RV.TRIGGER and performs Revaluation processing | DX.END.OF.DAY | FIN |
| 12 | DX.DEL.LIMIT.ETD | Limit updation for ETD trades is controlled based on parameter setup | DX.END.OF.DAY | FIN |
| 13 | DX.SOD.CUST.POS.REBUILD | Updates the file DX.CUST.POS | DX.START.OF.DAY | FIN |
| 14 | DX.UPDATE.CONTRACT.DATES | Updates the contract dates file | DX.UPDATE.CONTRACT.DATES | INT |
| 15 | DX.UPDATE.CONTRACT.DATES | Updates the contract dates file | DX.END.OF.DAY | FIN |
| 16 | DX.MKT.PRI.TO.HIST | Update the information to history file of market price record | DX.END.OF.DAY | FIN |
| 17 | DX.BUILD.TXN.ACT.CUST | Updates DX.TXN.ACT.CUST and clears file DX.TXN.ACT.CUST.WRK | DX.END.OF.DAY | FIN |
| 18 | DX.POST.PREM.SWAP.CDS | Posts the premium and moves the paid premium details from DX.PREMIUM.DETS file to DX.PREM.DETS.PAID file | DX.START.OF.DAY | FIN |
| 19 | DX.COB.PRICE.CHECK | Price Checking Process | DX.END.OF.DAY | FIN |
| 20 | DX.FWD.POST | Own-book P&L entries with forward value dates (i.e. charges/premswith posting offsets) are stored in DX.FWD.POSTINGS by transaction and value date. This process picks up postings due today and passes them to the Derivatives accounting. | DX.END.OF.DAY | FIN |
| 21 | DX.COB.CO.SYSTEM | To generate Automatic Closeouts | DX.END.OF.DAY | FIN |
| 22 | DX.SOD.RPA.TIDY | This job has a dependency on DX.SOD.RP.REBUILD | DX.START.OF.DAY | FIN |
| 23 | DX.FWD.POST.SOD | Own-book P&L entries with forward value dates (i.e. charges/premswith posting offsets) are stored in DX.FWD.POSTINGS by transaction and value date. This process picks up postings due today and passes them to the Derivatives accounting. | DX.START.OF.DAY | FIN |
| 24 | DX.COB.MARKET.PRICES | To purge the file DX.MARKET.PRICE | DX.END.OF.DAY | FIN |
| 25 | DX.POST.VM.INDIV.ENTRIES | Selects records with TRADE.STATUSRNA from DX.VARIATION.MARGIN.DETS | DX.RV.SERVICE | FIN |
| 26 | DX.POST.VM.INDIV.ENTRIES | Selects records with TRADE.STATUSRNA from DX.VARIATION.MARGIN.DETS | DX.END.OF.DAY | FIN |
| 27 | DX.COB.BUILD.WORKFILE | Updates the work file DX.COB.WORKFILE | DX.END.OF.DAY | FIN |
| 28 | DX.POST.CASH.PAYOUT | Updates DX.REP.POSITION and creates accounting entries for DX.CLOSEOUT | DX.POST.CASH.PAYOUT | FIN |
| 29 | DX.MTM.PROCESSING | - This rotuine gets the trade id as incoming argument and finds whether MTM is required or   not. - If MTM is required then fetch the market price key that is updated in trade and get the MTM   that is   - Updated in SYDX.MARKET.VAL record.   - Build the accounting entry for the MTM amount by calling DX.ACCOUNTING and then pass     the accounting   - Array to EB.ACCOUNTING to generate the accounting entries. | DX.END.OF.DAY | FIN |
| 30 | DX.ORD.AGR.TRADE | COB processing routine to do trade aggregation from order for derivatives | DX.ORD.AGR.TRADE | FIN |
| 31 | DX.CLEAR.FILES | This job is to clear the concat files of DX during COB processing | DX.START.OF.DAY | FIN |

## Digital Investments/Dual and Triple Currency Investments (DI)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | SY.DCI.EMIT | This routine handles the generation of IF events after maturity of SY.DCI contract | SY.DCI.EMIT | FIN |

## Direct Debits (DD)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | DD.DDI.AUTO.CANCEL | Moves the status from mandate to cancelled based on the inactivity period or termination date | DD.DDI.AUTO.CANCEL | FIN |
| 2 | DD.DDI.PURGE | Archives the DD.DDI with status as CANCELLED | DD.DDI.PURGE | FIN |
| 3 | DD.GENERATE.FILES | Processes the list of mandates and builds the required output file | DD.GENERATE.FILES | FIN |
| 4 | DD.PROC.COMB.RET | Processes DD return for combined item | DD.PROC.COMB.RET | FIN |

## Equity Accumulator (DP)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | SY.ENTL.CREATE | Job creates SY.ENTITLEMENT record | SY.CORPORATE.ACTIONS | FIN |
| 2 | SY.BTB.ENTL.CREATE | Job creates SY.B2B.ENTL record | SY.CORPORATE.ACTIONS | FIN |

## European Savings Directive (ET)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | SC.EU.DATA.BUILD.3 | This routine does the final EU tax calculation | INITIAL.DATA.BUILD | FIN |
| 2 | SC.EU.DATA.BUILD.3 | This routine does the final EU tax calculation | ET.END.OF.DAY | FIN |
| 3 | SC.EU.INFO.CUSTOMER | This routine builds the initial data for the tax calculation | ET.END.OF.DAY | FIN |
| 4 | SC.EU.DATA.BUILD.2 | Updates the work file SC.EU.DATA.BUILD.2 for the tax calculation | INITIAL.DATA.BUILD | FIN |
| 5 | SC.EU.DATA.BUILD.1 | Updates the work file SC.EU.DATA.BUILD.1 for the tax calculation | INITIAL.DATA.BUILD | FIN |
| 6 | SC.EU.PAST | Updates the file EU.TAX.LINK.PAST that needs to be purged | ET.END.OF.DAY | FIN |

## Fiduciary Deposits (FD)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | FD.EOD.PERFORM.ACCRUALS | Processes the accruals for interest and commissions for fiduciary contracts at the frequency defined in the parameter file. Selection file: FD.FIDUCIARY FD.FID.ORDER | FD.END.OF.DAY | FIN |
| 2 | FD.EOD.PROCESS.SCHEDULES | Processes all types of schedules corresponding to Placement and Fiduciary Order contracts. Selection file: FD.EOD.LIST FD.SCHEDULES | FD.END.OF.DAY | FIN |
| 3 | FD.SOD.PROCESS.SCHEDULES | Processes all types of schedules corresponding to Placement and Fiduciary Order contracts during split month end. Selection file: FD.EOD.LIST FD.SCHEDULES | FD.START.OF.DAY | FIN |
| 4 | FD.UPDATE.GROUP.PAYMENT | Updates FD.GROUP.PAYMENT records with AUTO.CHG.RATE set to 'Y' with the rate with the BID.RATE from PERIODIC.INTEREST table. Selection file: FD.GROUP.PAYMENT | FD.END.OF.DAY | FIN |
| 5 | FD.COMPLETE.AUTHORISATION | Performs authorisation process for the FIDUCIARY contract and the linked orders. Selection file: FD.FIDUCIARY$NAU | FD.END.OF.DAY | FIN |
| 6 | FD.EOD.UPDATE.CUST.VALUE | Calculates the total assets of each fiduciary customer portfolio's and stores it in the FD.CUST.VALUE file. Selection file:FD.ORDER.CUST | FD.END.OF.DAY | FIN |
| 7 | FD.SOD.PERFORM.ACCRUALS | Processes the accruals for interest and commissions for fiduciary contracts at the frequency defined in the parameter file during split month end. Selection file: FD.FIDUCIARY FD.FID.ORDER | FD.START.OF.DAY | FIN |
| 8 | FD.EOD.NOTICE.SCHEDULES | Processes all placements linked to the FD.GROUP.PAYMENT record and regenerate the next set of schedules for those contracts when FD.GROUP.PAYMENT record is changed. Selection file: FD.GROUP.PLACEMENT FD.GROUP.TODAY | FD.END.OF.DAY | FIN |
| 9 | FD.PROCESS.RENEWALS | Generate renewals of Fiduciary orders prior to maturity of the existing orders based on the value of RENEWAL.DAYS in FD. PARAMETER. Selection file: FD.ORDER.MATURITY | FD.START.OF.DAY | FIN |
| 10 | FD.EOD.STATIC.CHANGES | Process static changes for the fiduciary module. Changes to FD.FID.ORDER FD.FIDUCIARY and FD.PARAMETER as well as Customer level changes are processed. | FD.END.OF.DAY | FIN |
| 11 | FD.EOD.CYCLE.GROUP.PAYMENT | Cycles the interest settlement date in FD.GROUP.PAYMENT records. At the end of each interest settlement the details of rates are written to the FD.GROUP.PAYMENT.HIST file. Selection file: FD.GROUP.PAYMENT | FD.EOD.CYCLE.DATA | CUS |
| 12 | FD.EOD.REPLACE.ORDER | Replaces the orders based on REPLACE.ORDER field in FD.FID.ORDER. Selection file: FD.FID.ORDER | FD.END.OF.DAY | FIN |
| 13 | FD.UNPLACED.ORDERS | Generates new forward entries for those orders that are still unplaced but have passed the value date or have a principal change which has not yet been approved by the dealer and is back valued. Selection file: FD.FID.ORDER | FD.START.OF.DAY | FIN |
| 14 | FD.EOD.LIQ.TO.HIS | Moves the matured contracts to history based on DAYS.POST.MATURITY in parameter. Selection file: FD.FIDUCIARY FD.FID.ORDER | FD.END.OF.DAY | FIN |
| 15 | FD.FID.ORDER.LIQ.LIST | Get the FD order IDs which are matured as part of COB to be consumed by TAP | FD.START.OF.DAY | FIN |

## Funds Transfer (FT)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | FT.BULK.ARCHIVE | Moves the processed and rejected FT.BULK.MASTER and FT.BULK.ITEM records to HIS | FT.BULK.ARCHIVE | FIN |
| 2 | FT.BULK.PAYMENT | Performs bulk processing of FT based on set-ups in FT.BULK.MASTER and FT.BULK.ITEM | FT.BULK.PAYMENT | FIN |
| 3 | PAYMENT.BULK.CANCEL | Selects DISCARDED records in FT.BULK.MASTER and triggers their corresponding PAYMENT.ORDER to be moved to CANCELLED status | PAYMENT.BULK.CANCEL | FIN |
| 4 | PAYMENT.BULK.MASTER | Selects WAITEXEC records in FT.BULK.MASTER and triggers their corresponding PAYMENT.ORDER | PAYMENT.BULK.MASTER | FIN |
| 5 | CSM.BATCH.PROCESS.SERVICE | Processes CSMBATCH clearing messages | CSM.BATCH.PROCESS.SERVICE | FIN |
| 6 | FT.RATES.FIXING.PROCESS | Performs rate fixing for the INORATE and ANORATE records in FT.NORATE table | FT.RATES.FIXING.PROCESS | FIN |
| 7 | FT.SIM.EXPIRED.ARCHIVE | Deletes simulation expiry FT | FT.SIM.EXPIRED.ARCHIVE | FIN |

## General Ledger (RE)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | EOD.RE.CONTRACT.REVALUATION | Emits data to the reporting database for revaluation done at the contract level | EOD.RE.CONTRACT.REVALUATION | FIN |
| 2 | RE.DF.RECALC.ENTRY.LINE | Job record routine that exposes the financial details movement by re-stamping the new gl line for all the entries that are processed today | RE.DF.RECALC.ENTRY.LINE | FIN |
| 3 | RE.FIN.REPORTING.TAKEON | Retrieves information like PL movement, contract movement, GL Balance and ECB balance to IF | RE.FIN.REPORTING.TAKEON | FIN |
| 4 | RE.RETURN.EXTRACT | Builds the RE.CRF flat file for building CRB reports | RE.RETURN.EXTRACT | FRP |
| 5 | RE.BASE.CCY.CRF.SERVICE | Generates a balanced CRF base in any currency other than the LCYCRF.SERVICE | RE.BASE.CCY.CRF.SERVICE | FRP |
| 6 | UPDATE.PL.CLOSE.DATES.SERVICE | Updates missing PLclose dates in PL.CLOSE.DATES | UPDATE.PL.CLOSE.DATES.SERVICE | FIN |

## Interest & Charges (IC)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | GROUP.ACCRUAL.ONLINE | Rebuilds GROUP.ACCRUAL.DETAIL for the accounts which have moved during day and end of day processing | GROUP.ACCRUAL.ONLINE | FIN |
| 2 | CONV.AC.UPDATE.IC.CHARGE | One time service that runs during upgrade to update the IC.CHARGE ID in account record if WAIVE.ALL is 'Yes' | CONV.AC.UPDATE.IC.CHARGE | FIN |

## ISO20022 - ACCOUNT REPORTING (IX)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | XML.TRANSFORMATION | Generates CAMT messages based on the XML message from IF and XSL from EB.TRANSFORM | XML.TRANSFORMATION | INT |

## Limits (LI)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | LI.COLLATERAL.ACCOUNTING | Updates collateral type balances in ECB for respective limit | LI.COLLATERAL.ACCOUNTING | CUS |
| 2 | LI.CUSTOMER.GROUP.INFO.SERVICE | Updates the limit liablity when customer group is defined | LI.CUSTOMER.GROUP.INFO.SERVICE | CUS |
| 3 | LI.LIMIT.PARAMETER.MIGRATE | One time post upgrade service that creates new records in Limit parameter for each application from System record | LI.LIMIT.PARAMETER.MIGRATE | CUS |
| 4 | LI.PROCESS.REPORTING.INFO.SERVICE | Processes LIMIT.ALTERNATIVE.KEY to get validation limits of the particular customer or group | LI.PROCESS.REPORTING.INFO.SERVICE | CUS |
| 5 | LI.CONTRACT.ALLOCATION.SERVICE | Updates the limit and Collateral related details in ECB when there is any change in the structure | LI.CONTRACT.ALLOCATION.SERVICE | FIN |
| 6 | LIMIT.GROUP.RECALC.SERVICE | Processes the limit changes online whenever recalculation is required and based on a trigger file | LIMIT.GROUP.RECALC.SERVICE | CUS |
| 7 | LI.PROCESS.CHARGE.ACCT.SERVICE | Processes charge account removal from limit | LI.PROCESS.CHARGE.ACCT.SERVICE | CUS |
| 8 | LIMIT.UPDATE.SERVICE | Updates the limit exposure details of information type limits when they are setup to update the details as an offline process | LIMIT.UPDATE.SERVICE | CUS |
| 9 | LI.REBUILD.RESTRICTION.LIMITS | Updates restriction limits with effective date lying between next calender date and next working date | LI.REBUILD.RESTRICTION.LIMITS | CUS |

## Loans and Deposits (LD)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | LD.START.OF.DAY.3 | Processes accruals during end of day based on the accrual frequency in LD Parameter file during split month end and start of day .Selection file: LD.LOANS.AND.DEPOSITS | LD.START.OF.DAY | FIN |
| 2 | LD.START.OF.DAY.2 | Processes accruals for floating rate type contracts during split month end and start of day. Selection file: LD.LOANS.AND.DEPOSITS | LD.START.OF.DAY | FIN |
| 3 | LD.EOD.ISSUE.REIMB.ACCRUAL | Performs accrual or amortisation of issue and re imbursement price discount or premium.Selection file:LD.LOANS.AND.DEPOSITS | LD.END.OF.DAY | FIN |
| 4 | LD.EOD.ISSUE.REIMB.ACCRUAL | Performs accrual or amortisation of issue and re imbursement price discount or premium.Selection file:LD.LOANS.AND.DEPOSITS | LD.START.OF.DAY | FIN |
| 5 | LD.SOD.TRANCHE.END.SCH | Job to process the tranche end dates during split-month. | LD.START.OF.DAY | FIN |
| 6 | BR.EOD.LIQ.TO.HIS | To liquidate BILL REGISTER records to History | BR.END.OF.DAY | FIN |
| 7 | LD.PERIODIC.ADJUSTMENTS | Applies back dated rate changes in LD cont racts of periodic automatic type to the interest due to ch anges in PERIODIC.INTEREST tab le.Selection file: LD.LOANS.AND.DEPOSITS | LD.END.OF.DAY | FIN |
| 8 | LD.EOD.5 | Moves the matured contracts to history based on DAYS.POST.MATURITY field in LM M.INSTALL.CONDS file. Selection file:LD.LOANS.AND.DEPOSITS | LD.END.OF.DAY | FIN |
| 9 | LD.END.OF.DAY.2 | Processes accruals during end of day based on the accrual frequency in LD Parameter file.Selection file: LD.LOANS.AND.DEPOSITS | LD.END.OF.DAY | FIN |
| 10 | LD.SOD.FWD.MOVEMENT | Raises forward entries for the contracts in which the value date is adjust ed through VD.DATE.ADJUSTEMEN T field.Selection file:LD.LOANS.AND.DEPOSITS | LD.START.OF.DAY | FIN |
| 11 | LD.START.OF.DAY.1 | Processes all types of schedules in LD during split month end and start of day.Also process contracts with MAURE.AT. SOD is set to 'YES'.Selection file: LMM.SCHEDULESLD.COMMITMENT | LD.START.OF.DAY | FIN |
| 12 | LD.END.OF.DAY.8 | Processes the maturity of the commitment contracts. Selection file: LD.BACKVALUE.SCH.CONCAT LD.LOANS.AND.DEPOSITS | LD.END.OF.DAY | FIN |
| 13 | LD.END.OF.DAY.8 | Processes the maturity of the commitment contracts. Selection file: LD.BACKVALUE.SCH.CONCAT LD.LOANS.AND.DEPOSITS | LD.START.OF.DAY | FIN |
| 14 | LD.EOD.9 | Updates the new interest rate and interest amount for floating type LD contracts when the corresponding BI table is changed.Selection file: LD.LOANS.AND.DEPOSITS | LD.END.OF.DAY | FIN |
| 15 | LD.END.OF.DAY.4 | Processes all types of the schedules in LD module (loans deposits and commitments ) during end of day. Control list -Back (Back valued commitments) COMMITMENT(Normal commitments) Normal loans and deposits. Selection file: LD.BACKVALUE.SCH.CONCAT LMM.SCHEDULES LD.COMMITMENT | LD.END.OF.DAY | FIN |
| 16 | LD.SOD.COMMT.UPD | Updates the Commt.Avail.Amt in the commitment contracts during start of day for live tranche. Selection file: LD.TRANCHE.ST.LIST | LD.START.OF.DAY | FIN |
| 17 | LD.END.OF.DAY.3 | Processes accruals for floating rate type contracts. Selection file: LD.LOANS.AND.DEPOSITS | LD.END.OF.DAY | FIN |

## Lombard Lending (OV)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | OV.ONLINE.VAL.BASE | This record routine selects all the portfolios having holdings in the Security which has undergone a price change and update the activation file OV.ONLINE.VAL.FINAL.LIST. | OV.ONLINE.VAL.BASE | FIN |
| 2 | OV.ONLINE.VAL.FINAL | This record routine performs the real time valuation of the portfolio. | OV.ONLINE.VAL.FINAL | FIN |
| 3 | OV.ONLINE.VAL.BULK | This is the record routine of the multithreaded batch job OV.ONLINE.VAL.BULK. | OV.ONLINE.VAL.BULK | FIN |

## Nostro Reconcilliation (NR)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | NR.AUTOMATCH | Performs automatch of records in NR.ITEMS based on parameters defined in NR.PARAMETER | NR.AUTOMATCH | FIN |
| 2 | NR.PROCESS.MESSAGES | Processes the incoming MT messages to create Ledger and Statement type of records in NR.STATEMENTS and their corresponding NR.ITEMS | NR.PROCESS.MESSAGES | FIN |

## Past Due (PD)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | PD.PROCESS.OP.BALANCES | Updates the existing PD.BALANCES record when th e PD.PEN.CALC.BASIS not equal to POST.GR.PE.CALC then the penalty interest will be calculated based on the new base amo unt. Selection file:PD.OP.BALANCES.DATE.LIST | PD.EOD.PRE.PROCESS | FIN |
| 2 | PD.PROCESS.OP.BALANCES | Updates the existing PD.BALANCES record when th e PD.PEN.CALC.BASIS not equal to POST.GR.PE.CALCthen the penalty interest will be calcul ated based on the new base amount. Selection file: PD.OP.BALANCES.DATE.LIST | PD.END.OF.DAY | FIN |
| 3 | PD.PROCESS.OP.BALANCES | Updates the existing PD.BALANCES record when th e PD.PEN.CALC.BASIS not equal to POST.GR.PE.CALCthen the p enalty interest will be calcul ated based on the new base amount. Selection file: PD.OP.BALANCES.DATE.LIST | PD.START.OF.DAY | FIN |
| 4 | PD.EOD.ACTIVITY.TODAY | Processes charges and commissions for all PD's that were created during the day. Selection file: PD.ACTIVITY.TODAY | PD.END.OF.DAY | FIN |
| 5 | PD.EOD.CONTRACT | Process all activities for PD contracts - This includes limit processing retry of payment floating rate changes capitalisation and accrual postings movement to history etc. Selection file: PD.PAYMENT.DUE. Control list: PROCESS.PDS(to process pd records) PURGE.EXCEPTION ( to delete PD.PROV.EXCEPTION.LOG) file | PD.END.OF.DAY | FIN |
| 6 | PD.PROCESS.AC.PD | Processes 'PR''IN' type of PDAC contracts and adjusts PD balances based on underlying account's movements .Selection file: OD.ACCT.ACTIVITY | PD.SYS.END.OF.DAY | FIN |
| 7 | PD.UNDER.REV.SUSP | Program to reverse the accruals | PD.EOD.PRE.PROCESS | FIN |
| 8 | PD.UNDER.REV.SUSP | Program to reverse the accruals | PD.END.OF.DAY | FIN |
| 9 | PD.EOD.DEL.PD.CAP | Moves l PD.CAPTURE records to history . Selection file: PD.CAPTURE | PD.END.OF.DAY | FIN |
| 10 | PD.EOD.AC.OD | Creates PDAC for Account PDs. Selection file: ACCOUNT.OVERDRAWN | PD.SYS.END.OF.DAY | FIN |
| 11 | PD.UNDER.REV.ACC | To reverse the accruals | PD.EOD.PRE.PROCESS | FIN |
| 12 | PD.UNDER.REV.ACC | To reverse the accruals | PD.END.OF.DAY | FIN |
| 13 | PD.UNDER.REV.ACC | To reverse the accruals | PD.START.OF.DAY | FIN |
| 14 | PD.AC.OD.CLEAR | Repays thePDAC contract for which account is out of overdraft. Selection file:PD.EOD.AC.OD.PREVIOUS | PD.SYS.END.OF.DAY | FIN |
| 15 | PD.PROCESS.PAYMENT | Processes repayments for PDs triggered by online payment.Selection file: PD.ONLINE.PAYMENT | PD.END.OF.DAY | FIN |
| 16 | PD.PROCESS.UL.MVMT | Adjusts the underlying contract's principal movement amount in the corresponding PD balances records with calc basis is OS. Selection file:PD.OS.PRINC.MVMT | PD.EOD.PRE.PROCESS | FIN |
| 17 | PD.PROCESS.UL.MVMT | Adjusts the underlying contract's principal movement amount in the corresponding PD balances records with calc basis is OS. Selection file: PD.OS.PRINC.MVMT | PD.END.OF.DAY | FIN |
| 18 | PD.PROCESS.UL.MVMT | Adjusts the underlying contract's principal movement amount in the corresponding PD balances records with calc basis is OS. Selection file: PD.OS.PRINC.MVMT | PD.START.OF.DAY | FIN |
| 19 | BACK.VALUE.SUSPENSION | Reverse out the accurals that have been posted to P&L for the suspended record. | PD.EOD.PRE.PROCESS | FIN |
| 20 | PD.SOD.CONTRACT | Process all activities for PD contracts during start of day of split month end - This includes limit processing retry of payment floating rate changes capitalisation and accrual postings movement to history etc. Selection file: PD.PAYMENT.DUE. Control list:PROCESS.PDS | PD.START.OF.DAY | FIN |

## Pricing in AA (PR)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | AA.CUSTOMER.RELATIONSHIP.TRACKER | Looks for the relationship products against which arrangement has to be raised for the incoming Customer ID. There can be cases where the customer might be checked against multiple products. In such cases, all the products are processed in one call to process this job. | BNK/AA.CUSTOMER.RELATIONSHIP.TRACKER | FIN |
| 2 | AA.RELATIONSHIP.TRACKER | Tracks the Relationship product changes and applies them to the related customer arrangement record | BNK/AA.RELATIONSHIP.TRACKER | FIN |

## Repurchase Agreements (RP)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | RP.SOD.DETERMINE.ACTIVITY | Determines the contract initiation and maturity activities for the forward and live contracts | RP.START.OF.DAY | FIN |
| 2 | RP.SOD.MARGIN.CALL | Handles Margin Call in Repo | RP.START.OF.DAY | FIN |
| 3 | RP.EOD.MATURITY | Moves RP contracts to MAT | RP.END.OF.DAY | FIN |
| 4 | RP.SOD.STATUS.CHANGE | Routine to move FWD contracts to CUR if the value date is LE TODAY | RP.START.OF.DAY | FIN |
| 5 | RP.EOD.DETERMINE.ACTIVITY | Determines EOD REPO contract Maturity or Initiation | RP.END.OF.DAY | FIN |
| 6 | RP.SOD.LIQ.TO.HIS | One of the component of RP.SOD.PROCESSING | RP.START.OF.DAY | FIN |
| 7 | RP.MM.EOD | Processes MM capitalisation for MM contracts thro' REPO | RP.END.OF.DAY | FIN |
| 8 | RP.SOD.MATURITY | Processes Matured Repos. | RP.START.OF.DAY | FIN |
| 9 | RP.EOD.STATUS.CHANGE | Moves RP contracts FWD->CUR | RP.END.OF.DAY | FIN |
| 10 | RP.EOD.LIQ.TO.HIS | Moves the contracts to History after Settlement | RP.END.OF.DAY | FIN |
| 11 | RP.SOD.UPDATE.POSITIONS | Delete security.transfer references from RP.SCTR.UPD.SCHEDULES Called by REPO when replacement has occurred. | RP.START.OF.DAY | FIN |
| 12 | RP.EOD.MARGIN.CALL | Handles Margin Call in Repo | RP.END.OF.DAY | FIN |
| 13 | RP.EOD.SOD.DELIVERY | Runs delivery of REPO contracts in close of business | RP.END.OF.DAY | FIN |
| 14 | RP.EOD.SOD.DELIVERY | Runs delivery of REPO contracts in close of business | RP.START.OF.DAY | FIN |

## Retail Bundle (AB)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | AA.POOL.ADMINISTRATION.PROCESS | Performs pool administration operations link, delink and restructure of both external and internal | BNK/AA.EOD.POOL.ADMINISTRATION | FIN |
| BNK/AA.SOD.POOL.ADMINISTRATION | FIN |
| 2 | AA.POOL.ADMINISTRATION.RESUBMIT | Reschedules the activities that are failed to next working day | BNK/AA.SOD.POOL.ADMINISTRATION | FIN |
| 3 | AA.POOL.ORCHESTRATION.SERVICE | Orchestrates various activities within a balance netting pool | BNK/AA.POOL.ORCHESTRATION.PROCESS | FIN |
| BNK/AA.POOL.ORCHESTRATION.SERVICE | FIN |

## Retail Lending (AL)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | AA.SERVICE.PROCESS | Performs the processing of all scheduled activities. The process checks for all current arrangement contracts to see if there a scheduled activity due to be processed as part of the Close of Business. | AA.INTRADAY.PROCESS | FIN |
| AA.EOD.PROCESS | FIN |
| AA.SOD.PROCESS | FIN |
| 2 | AA.COB.PAY.IN.OUT | This job submits and completes the processing of AA.ARRANGEMENT.ACTIVITY requests generated by non-AA transactions during close of business | AA.SOD.PROCESS | FIN |

## Securities (SC)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | SC.PERF.DETAIL.UPD.BATCH | Updates SC.CASH.FLOW.TRANS and SC.PERF.DETAIL | SC.BATCH.PERF | FIN |
| 2 | AM.SC.MOVEMENT.TOTAL | It is one of the job in AM.SC.MOVEMENT batch which checks the total nominal available based on the valuation amount in SAM or closing nominal from SP for each OBC record and stores the corresponding record in another work file called FBNK.AM.SC.MOVEMENT.TOTS if nominal available. | AM.SC.MOVEMENT | FIN |
| 3 | SC.ACCR.DATE.UPDATE | Performs the interest day cycling in SECURITY.MASTER | SC.BATCH.START | FIN |
| 4 | SC.TRAIL.FEES.BV.UPDATE.POST | Clears BV.EFFECTIVE.DATE from all SC.TRAIL.FEES.ARRANGEMENT records | SC.TRAIL.FEES.BV.UPDATE | CUS |
| 5 | SC.TRAIL.FEES.BV.UPDATE.POST | Clears BV.EFFECTIVE.DATE from all SC.TRAIL.FEES.ARRANGEMENT records | SC.RECALC.TRAIL.FEES | CUS |
| 6 | SC.EOM.VAL.PRICE.UPD | Updates SC.VAL.PERFORM | SC.BATCH.REP | FIN |
| 7 | WRITE.SC.VAL.EXTRACT | Updates SC.VALUATION.EXTRACT file from SC.POS.ASSET file | SOD.SC.VAL.EXT | FIN |
| 8 | WRITE.SC.VAL.EXTRACT | Updates SC.VALUATION.EXTRACT file from SC.POS.ASSET file | SC.VAL.EXTRACT | FIN |
| 9 | SC.UPD.VALUE.DATE.POSN | Calculates value date position | SC.SYS.END.OF.DAY | FIN |
| 10 | SC.EOD.SETTLE.MAT | Moves matured SC.SETTLEMENT records to history | SC.SYS.END.OF.DAY | FIN |
| 11 | PURGE.OPEN.ORDER.DETAILS | Moves SC.SOO.CUST.DETAIL records to history when the parent SOO is moved to history | SC.BATCH.APP | FIN |
| 12 | SC.REVAL.PROCESSING.POST | Recycles the revaluation frequency | SC.BATCH.APP | FIN |
| 13 | SC.AM.DYN.MODEL.SYNC | Adjusts nominal amounts against securities on a nominal type dynamic model after corporate action has taken place. Shell for AM.DYN.MODEL.SYNC. | SOD.SC.VAL.EXT | FIN |
| 14 | SC.TRAIL.FEES.ACCR.POST | Posts the trailer fee accrual entries based on the setup in SC.TRAIL.FEES.ARRANGEMENT | SC.TRAIL.FEES.ADJUSTMENT | CUS |
| 15 | SC.TRAIL.FEES.ACCR.POST | Posts the trailer fee accrual entries based on the setup in SC.TRAIL.FEES.ARRANGEMENT | SC.EOD.TRAIL.FEES | CUS |
| 16 | SC.TRAIL.FEES.ACCR.POST | Posts the trailer fee accrual entries based on the setup in SC.TRAIL.FEES.ARRANGEMENT | SC.SOD.TRAIL.FEES | CUS |
| 17 | OL.VAL.REPS.CONSOLIDATE | Selects OL.VAL.REPS.CONS.INT and OL.VAL.REPS.CONS.EXT and generates internal and external reports based upon the report type. | OL.VAL.REPS | FIN |
| 18 | SC.OL.VAL.MASTER.MARGIN | Updates the group margin fields in the SEC.ACC.MASTER | SC.GROUP.VALUATION.MARGIN | FIN |
| 19 | SEC.TRADE.SERVICE | Updates the SEC.TRADE.CUST.DETAIL record through service | SEC.TRADE.SERVICE | FIN |
| 20 | SC.STOCK.DIV.RERUN | This subroutine, for each request key on the concat record, cancels or recreates the detail records for stock dividends depending on the value of the 'RERUN/CANCEL' flag on the request record. | SC.BATCH.APP | FIN |
| 21 | SC.EOD.TRADE.CALC.PL | Updates SC.SEC.ACC.PL with realized and unrealized profits for today trades | SC.BATCH.REP | FIN |
| 22 | SC.EXT.ASSETS.BAL | The Net Asset Balance is extracted from SC.POS.ASSET for the purpose of computing the Investment Advisory Charges. | SC.SYS.END.OF.DAY | FIN |
| 23 | SC.EOD.BLK.RECS | Records from the SC.BLOCK.SEC.POS file which have expired are moved to $HIS file and deletes the old records | SC.BATCH.APP | FIN |
| 24 | SC.EOD.EXCEPTION.LOG | Creates exception log for transaction overrides | SC.BATCH.REP | FIN |
| 25 | SC.SOD.SETT.DATE.ACCTG | Raises accounting at EOD of value date | SC.BATCH.START | FIN |
| 26 | SC.BULK.CHILD.AUTH.SERVICE | Authorises all the child orders/trades of the given parent order/trade. | SC.PARENT.CHILD.PROCESSING | FIN |
| 27 | EOD.VAL.PERFORM.UPDATE2 | Updates FLOW.AMOUNT and VALUATION FLOW in SC.VAL.PERFORM | SC.BATCH.REP | FIN |
| 28 | SC.PARENT.CHILD.TRADE.REV | Reverses Order records with information from REV work file | SC.PARENT.CHILD.TRADE.REV | FIN |
| 29 | SC.STOCK.CONV.SETTLE | Processes unsettled txns in the orig.sec during stock conversion | SC.BATCH.APP | FIN |
| 30 | SC.STOCK.CONV.SETTLE | Processes unsettled txns in the orig.sec during stock conversion | SC.CORPORATE.ACTIONS | FIN |
| 31 | SC.DIV.COUP.RERUN | This subroutine, for each request key on the concat record, cancels or recreates the detail records for coupons/dividends depending on the value of the 'RERUN/CANCEL' flag on the request record. | SC.BATCH.APP | FIN |
| 32 | SC.CLEAR.RECLASS.WRK | This routine deletes the Workfile SC.SAM.RECLASS.WRK after RECLASSIFICATION | SC.BATCH.APP | FIN |
| 33 | SC.ADV.FEES.ACCRUAL | Calculates ADVISORY fees. | SC.SYS.END.OF.DAY | FIN |
| 34 | SC.POS.MVMT.CLEAR | Deletes the SC.POS.MOVEMENT file | SC.SYS.END.OF.DAY | FIN |
| 35 | EOD.SCINDICES.UPDATE | EOD job routine to read Last.Price from Security.Master and updates c.idx.RATE in Sc.Indices | SC.SYS.END.OF.DAY | FIN |
| 36 | SP.PARENT.CHILD.DELIVERY | Process of child trades authorisation and regeneration on replacement of parent trade | SP.PARENT.OUTWARD.SETT | FIN |
| 37 | SC.PURGE.BUILD.POS | Updates SC.TRANS.POS.HISTORY and related accounting adjustment at SOD | SC.BATCH.START | FIN |
| 38 | SC.EOD.BROKER.POS.UPDATE | Updates the settlement of stock between broker and depository for contractual settlement | SC.BATCH.APP | FIN |
| 39 | SC.EOD.SDC.CALC.PL | Updates SC.SEC.ACC.PL with realized and unrealized profits for STOCK.DIV.CUS | SC.BATCH.REP | FIN |
| 40 | EOD.BUILD.CG.TXN.BASE | Initiates the build for the CG Transaction Base. | SC.BATCH.APP | FIN |
| 41 | EOD.OUTST.DELIVER | Runs at the end of the day and authorises the outstanding delivery records which satisfy certain conditions. It ignores any records whose is 'IHLD'. The incoming argument for this routine is SEC.DEL.CONTROL$NAU record ID | SC.BATCH.APP | FIN |
| 42 | AM.SC.MOVEMENT.PRE | It is one of the job in AM.SC.MOVEMENT batch which reads all the records from the work file FBNK.AM.SC.MOVEMENT.POST and deletes all the existing records from SC.OBC.CUST.DETAIL (both in live and exception). | AM.SC.MOVEMENT | FIN |
| 43 | SC.EOD.SUB.ACC.CHG.POST | Clears all the NEW.CHANGED fields from SC.SUB.ACC.ROUTING | SYSTEM.SECURITIES | CUS |
| 44 | SC.TRAIL.FEES.PRORATA.EXTRACT | Prorates the adjustment amount in the SC.TRAIL.FEES.HOLDING record across the individual client | SC.TRAIL.FEES.ADJUSTMENT | CUS |
| 45 | SC.PRICE.CHANGE.ARCHIVAL | Archival of SC.PRICE.CHANGE and SC.PRICE.CHANGE.CON | SC.INT.ARCHIVAL | INT |
| 46 | SC.UPDATE.SM.PRICE | Updates price field In SECURITY.MASTER | SC.BATCH.START | FIN |
| 47 | EOD.VAL.PERFORM.UPDATE1 | Updates PERFORM.FLOW VALUATION.END and PERFORM.END fileds in SC.VAL.PERFORM | SC.BATCH.REP | FIN |
| 48 | SC.SAFEKEEP.ACC | Generates safe keeping charges related to accounting | SC.SYS.END.OF.DAY | FIN |
| 49 | SC.SAFEKEEP.ACC | Generates safe keeping charges related to accounting | SC.BATCH.START | FIN |
| 50 | SC.OL.VAL.CHILD | Performs valuation for the portfolio needs to valuate group margin value calculation | SC.GROUP.VALUATION | FIN |
| 51 | SC.EOD.MT536.INITIATE | Initiates the generation of MT536 outbound message | SC.BATCH.STMT | FIN |
| 52 | SC.SAFE.FEES.ACCRUAL | Calculates SAFECUSTODY fees. | SC.SYS.END.OF.DAY | FIN |
| 53 | SC.PORT.DIVERS | Generate print file for portfolio diversification | SC.BATCH.REP | FIN |
| 54 | SC.FEE.REALISE | Realises safekeep/advisory fees | SC.SYS.END.OF.DAY | FIN |
| 55 | SC.FEE.REALISE | Realises safekeep/advisory fees | SC.BATCH.START | FIN |
| 56 | SR.TIDY.FILES | Subroutine to move reconciliation data from live to history files | SC.BATCH.RECON | CUS |
| 57 | SC.CALC.YIELD.CON | Calculates current yield YTM duration modified duration for all bonds and updates SECURITY.SUPP | SC.SYS.END.OF.DAY | FIN |
| 58 | SC.REVAL.PROCESSING | The unrealized p/l posted on the last working day is reversed. The current position is revalued with the last price and the unrealised profit/loss is calculated. Trading position is updated with unrlprofit and reval date. The unrealized p/l calculated is posted. The current realized p/l is also posted SC.PL.ACCT.SETUP is called for posting a/c entries | SC.BATCH.APP | FIN |
| 59 | SC.CLEAR.FILES | Clears some of the Securities files during COB processing | SC.EOD.REP | FIN |
| 60 | SC.CLEAR.FILES | Clears some of the Securities files during COB processing | SC.ONLINE | FIN |
| 61 | SC.TRAIL.FEES.BV.UPD.HOLDING | Updates the Holding Record during Back dated Transaction | SC.TRAIL.FEES.BV.UPDATE | CUS |
| 62 | SC.ENTITL.CREATE.POST | Updates Diary records with the information generated in the ENTITLEMENT record | SC.CORPORATE.ACTIONS | FIN |
| 63 | SC.TRADE.POS.ACCRUAL | Calculates the value dated position cost of position and accrued interest. Accounting entries are generated for daily accruals | SC.BATCH.APP | FIN |
| 64 | SC.AUTO.GRP.ORD | Automatically groups multiple Sec.open.orders into a single order only when GROUP.ORDER is set to 'Automatic' or 'Both' in Sc.Parameter | SC.GRP.ORD.SERVICE | FIN |
| 65 | SC.BOND.RED.RERUN | This subroutine for each request key on the concat record cancels or recreates the detail records for bond redemptions depending on the value of the 'RERUN/CANCEL' flag on the request record. | SC.BATCH.APP | FIN |
| 66 | SC.EOD.VAL.PERF.UPD | Updates SC.VAL.PERFORM with STMT.ENTRY data which are created today | SC.BATCH.REP | FIN |
| 67 | EOD.REDEM.WARN.LIST | Job to setup redemption requests for a security that is within the date range specified in SC.PARAMETER. | SC.BATCH.REP | FIN |
| 68 | SC.EOD.CHANGE.SUB.ASSET | This end of day routine is used to call SC.CHANGE.SUB.ASSET which updates all linked records whenever the SUB.ASSET.TYPE on a SECURITY.MASTER record changes. | SC.BATCH.APP | FIN |
| 69 | SC.ADV.FEES.CREATE | Routine for posting advisory charges as a service. | SC.ADV.FEES.POST | FIN |
| 70 | SC.PARENT.DEPO.CREATE | This job creates parent trade for group of depository involved in the order. | SC.PARENT.DEPO.CREATION | FIN |
| 71 | CONV.SC.HOLD.POS | Selects SC.HOLD.POS file and updates the SC.HOLD.POS file. | CONV.SC.HOLD.POS.R08 | FIN |
| 72 | SEC.OPEN.ORDER.LOG | Creates exception log for override details in SEC.OPEN.ORDER | SC.BATCH.REP | FIN |
| 73 | SEC.OPEN.ORDER.SERVICE.ROUND | Calculates and rounds the nominal's of SEC.OPEN.ORDER.SERVICE.ROUND records | SEC.OPEN.ORDER.SERVICE | FIN |
| 74 | SC.EOD.OPEN.BAL.UPDATE | Updates value dated and trade dated opening balance | SC.BATCH.START | FIN |
| 75 | PURGE.OPEN.ORDERS | Moves the live SOO to $HIS | SC.BATCH.APP | FIN |
| 76 | SC.ADV.FEES.MONTHLY.ACRL | Raises accrual entries of advisory fees based on the setup in SAFECUSTODY.VALUES | SC.SYS.END.OF.DAY | FIN |
| 77 | SC.WHT.ADJUSTMENT.SERVICE | Updates SC.PROCESS.WHT.ADJ record for selected Entitlements based on selection criteria | SC.WHT.ADJUSTMENT.SERVICE | FIN |
| 78 | OL.VAL.REPS.SERVICE | Selects OL.VAL.REPS records and generates reports depending upon the value REP.TYPE. | OL.VAL.REPS | FIN |
| 79 | SC.TRADE.POS.HIS.UPD | Updates SC.TRADE.POS.HISTORY | SC.BATCH.APP | FIN |
| 80 | SC.OL.VAL.MASTER.PLEDGE | Updates the pledge margin value to SC.VALUATION.GROUP | SC.GROUP.VALUATION.MARGIN | FIN |
| 81 | STOCK.DIV.LOG | Creates exception log for override details in STOCK.COUP.CUST and STOCK.COUP.DET | SC.BATCH.REP | FIN |
| 82 | SC.CASH.FLOW | Creates F.SC.CASH.FLOW.TRANS print file | SC.BATCH.REP | FIN |
| 83 | SC.GROUP.POS.ASSET.CLR | Clears the group positions | SC.GROUP.VALUATION | FIN |
| 84 | SC.GROUP.POS.ASSET.CLR | Clears the group positions | SC.SYS.END.OF.DAY | FIN |
| 85 | SC.TRAIL.FEES.REALISE | Raises Capitalisation entry on the Payment date | SC.EOD.TRAIL.FEES | CUS |
| 86 | SC.EXT.CLOSING.BAL | The Closing Balance value is extracted from the SECURITYPOSITION for the purpose of computing the safekeeping fees. | SC.SYS.END.OF.DAY | FIN |
| 87 | SC.SOD.APPLY.DEF.INSTR | Applies default instructions on ENTITLEMENT records that have no standing instructions | SC.ONLINE | FIN |
| 88 | SC.EOD.DCC.CALC.PL | Updates SC.SEC.ACC.PL with realized and unrealized profits for DIV.COUP.CUS | SC.BATCH.REP | FIN |
| 89 | WRITE.SC.VAL.EXTRACT.FXSUSP | Updates account related SC.VALUATION.EXTRACT records when the DIVERT.SPOT is set as YES | SOD.SC.VAL.EXT | FIN |
| 90 | WRITE.SC.VAL.EXTRACT.FXSUSP | Updates account related SC.VALUATION.EXTRACT records when the DIVERT.SPOT is set as YES | SC.VAL.EXTRACT | FIN |
| 91 | SC.CHILD.TRADE.AUTH | This job authorises child trades by checking whether parent trade is authorised | SC.PARENT.TRADE.AUTHORISE | FIN |
| 92 | FD.EOD.UPDATE.CUST.VALUE | Calculates the total assets of each fiduciary customer portfolio's and stores it in the FD.CUST.VALUE file. Selection file: FD.ORDER.CUST | SC.SYS.END.OF.DAY | FIN |
| 93 | SC.EOD.CASH.FLOW.TRANS | Updates SC.CASH.FLOW.TRANS file for each STMT.ENTRY found in ACCT.ENT.TODAY | SC.BATCH.PERF | FIN |
| 94 | SC.UPD.TRAIL.FEES.ARRANGEMENT | Updates the Accrued amount in SC.TRAIL.FEES.ARRANGEMENT record on each Calculation date | SC.TRAIL.FEES.BV.UPDATE | CUS |
| 95 | SC.UPD.TRAIL.FEES.ARRANGEMENT | Updates the Accrued amount in SC.TRAIL.FEES.ARRANGEMENT record on each Calculation date | SC.EOD.TRAIL.FEES | CUS |
| 96 | CONV.SC.HOLD.POS.POST | Selects SC.HOLD.POS file and deletes the SC.HOLD.POS file | CONV.SC.HOLD.POS.R08 | FIN |
| 97 | REDEMPTION.LOG | Creates exception log for override details in REDEMPTION.CUST and REDEMPTION.DET | SC.BATCH.REP | FIN |
| 98 | SEC.OPEN.ORDER.SERVICE.PRE | Creates $nau records from live when a parent SOO has been re-input or reversed | SEC.OPEN.ORDER.SERVICE | FIN |
| 99 | SC.CPMF.ADC.PRATA.CALC | Calculates Advisory charges on Grouped portfolios with charge type as PRORATA | SC.SYS.END.OF.DAY | FIN |
| 100 | WRITE.SC.VAL.PEND | Updates the valuation for the pending order | SOD.SC.VAL.EXT | FIN |
| 101 | WRITE.SC.VAL.PEND | Updates the valuation for the pending order | SC.VAL.EXTRACT | FIN |
| 102 | SC.UPD.STP.BALANCES | Updates Contract Balance File of SC (SC.TRADING.POSIITON) with CONSOL.TRADING.BALANCE and CONTINGENT.BAL.CR and CONTINGENT.BAL.DB depending on Trans Type.(LIVE and FORWARDCR and FORWARDDB) | SC.BATCH.APP | FIN |
| 103 | WRITE.SC.VAL.EXTRACT.PRE | Pre routine for clearing the SC.VALUATION.EXTRACT and the SC.VALUATION.EXTRACT.CONCAT file. | SOD.SC.VAL.EXT | FIN |
| 104 | WRITE.SC.VAL.EXTRACT.PRE | Pre routine for clearing the SC.VALUATION.EXTRACT and the SC.VALUATION.EXTRACT.CONCAT file. | SC.VAL.EXTRACT | FIN |
| 105 | SC.SAFE.FEES.MONTHLY.ACRL | Raises accrual entries of safekeeping fees based on the setup in SAFECUSTODY.VALUES | SC.SYS.END.OF.DAY | FIN |
| 106 | SC.EOD.SUB.ACC.CHG | Updates the existing positions with a sub account according to the set-up for SC.SUB.ACC.ROUTING file. | SC.BATCH.APP | FIN |
| 107 | SC.UPDATE.SUPP | Calculates and updates field *Price Earn Ratio* in Security.Supp with the PRICE passed. | SC.CLEAR.CASHFLOW | FIN |
| 108 | SC.STOCK.ENTRY.CLEAR | Clears SC.STOCK.ENTRY file | SC.BATCH.REP | FIN |
| 109 | SC.CI.RERUN | This subroutine for each request key on the concat record cancel or recreate the detail records for capital increase depending on the value of the 'RERUN/CANCEL' flag on the request record . | SC.BATCH.APP | FIN |
| 110 | SC.DIARY.REVERSAL | Handles both Entitlement Reversals/Deletions thru OFS during a DIARY reversal. | SC.CORPORATE.ACTIONS | FIN |
| 111 | SC.OL.VAL.SEC | Performs portfolio valuation and to recalculate and update the Security position | SC.SYS.END.OF.DAY | FIN |
| 112 | SC.CONSOL.SWITCH | Switching of consol keys based on the amounts and updates the SC.TRADING.POSITION record | SC.BATCH.APP | FIN |
| 113 | SC.EOD.ORDER.BY.CUST | Moves OBC records to history | SC.BATCH.REP | FIN |
| 114 | SC.ENTITLE.CREATE | Generates/authorises Entitlement records | SC.CORPORATE.ACTIONS | FIN |
| 115 | SC.CPMF.SKF.SINGLE.CALC | SC.CPMF.SKF.SINGLE.CALC Safekeeping fees on Grouped portfolios with charge type as SINGLE. | SC.SYS.END.OF.DAY | FIN |
| 116 | SC.EOM.UPDATE | Updates SAM with performance details and also SC.SEC.ACC.PL | SC.BATCH.REP | FIN |
| 117 | EB.COMM.ACCRUAL.SC | Accrual of safekeeping and advisory charges | SC.SYS.END.OF.DAY | FIN |
| 118 | SC.SOD.RECALC.PRICES | Start of Day stage program to recalculate the prices and yield percentages from today to maturity | SC.SYS.END.OF.DAY | FIN |
| 119 | SC.CHECK.SEC.CONS | Checks the violation of Holding Restrictions during Batch | SOD.SC.VAL.EXT | FIN |
| 120 | SC.EOD.TRAIL.FEES.ACCRUAL | Calculates the trailer fee amount which is due from the issuer | SC.EOD.TRAIL.FEES | CUS |
| 121 | SC.EOD.VALUE.DT.STK.POS | Updates of SC.STOCK.POSITION file with long or short position based on the transaction type. | SC.BATCH.APP | FIN |
| 122 | SC.EOD.PERF.POLICY | ROUTINE TO UPDATE THE PERFORMANCEPOLICY FILE | SC.BATCH.REP | FIN |
| 123 | SC.SOD.STOCK.CONV.SETTLE | Processes unsettled txns in the orig.sec during stock conversion | SC.BATCH.START | FIN |
| 124 | SC.RECALC.SEC.POSN | Rebuilds and recalculates security positions and security trans | SC.SYS.END.OF.DAY | FIN |
| 125 | SC.TRAIL.FEES.RECALC.EXTRACT | Recalculates the Extract record because of Back Dated Transactions | SC.TRAIL.FEES.BV.UPDATE | CUS |
| 126 | SC.TRAIL.FEES.RECALC.EXTRACT | Recalculates the Extract record because of Back Dated Transactions | SC.RECALC.TRAIL.FEES | CUS |
| 127 | SC.AM.CLR.SCE.SERVICE | Clears down old records from AM.SCENARIO and AM.COMPARE.DETAIL. | AM.SC.MOVEMENT | FIN |
| 128 | SC.MANUAL.GRP.ORD | Selects the work file Sc.Manual.Grp.Ord.Wrk and Groups multiple Sec.Open.Orders into a single record through service | SC.GRP.ORD.SERVICE | FIN |
| 129 | SP.PARENT.CHILD.SETTLE | This routine settles child reconciliation record on settlement of parent reconciliation | SP.PARENT.INWARD.SETT | FIN |
| 130 | SC.SETTLEMENT.SERVICE.PRE | Start of the sc.settlement service selects all records set for processing and moves them to the post file. | SC.SETTLEMENT.SERVICE | FIN |
| 131 | SC.EOD.DELIV.POST | Send all pending messages to delivery handoff | SC.BATCH.REP | FIN |
| 132 | AM.SC.MOVEMENT.POST | It is one of the job in AM.SC.MOVEMENT batch which AM.SC.MOVEMENT batch which round the nominal from each OBC record by reading the record from FBNK.AM.SC.MOVEMENT.ROUNDING work file and update it in FBNK.SC.OBC.CUST.DETAIL file. It also delete the record from FBNK.AM.SC.MOVEMENT.ROUNDING work file after the process gets completed | AM.SC.MOVEMENT | FIN |
| 133 | SC.ORD.TRD.FWD.ACCT | Raises fwd entry for trades (moved from Inau to Ihld) that are created from orders. | SC.BATCH.START | FIN |
| 134 | SEC.OPEN.ORDER.SERVICE | Processes the SOO records to move from IHLD to INAU or INAU to LIVE | SEC.OPEN.ORDER.SERVICE | FIN |
| 135 | SC.ENTITLE.MODIFY | Updates price on Entitlement records. | SC.CORPORATE.ACTIONS | FIN |
| 136 | SC.PARENT.CHILD.ORDER.REV | Reverses order records with the information from rev work file. | SC.PARENT.CHILD.ORDER.REV | FIN |
| 137 | DIV.COUP.LOG | Creates exception logfor override details in DIV.COUP.CUST and DIV.COUP.DET | SC.BATCH.REP | FIN |
| 138 | SEC.TRADE.SERVICE.PRE | Selects routine to setup the common area for the multi-threaded COB job SEC.TRADE.SERVICE.PRE | SEC.TRADE.SERVICE | FIN |
| 139 | SC.SETT.DATE.ACCTG | Raises the settlement dated accounting entries for future dated transactions | SC.BATCH.APP | FIN |
| 140 | SC.SAFE.FEES.ACC | Generates management fees related accounting | SC.SYS.END.OF.DAY | FIN |
| 141 | SC.SAFE.FEES.ACC | Generates management fees related accounting | SC.BATCH.START | FIN |
| 142 | SC.SOD.BROKER.POS.UPDATE | Records settlement between broker and depository for actual settlement | SC.BATCH.START | FIN |
| 143 | SC.EOD.FUND.FLOW | Updates SC.CASH.FLOW.TRANS file for each STMT.ENTRY found in ACCT.ENT.TODAY | SC.BATCH.REP | FIN |
| 144 | SC.UPDATE.SUPP.POST | Clears market.price | SC.CLEAR.CASHFLOW | FIN |
| 145 | SC.POSITION.STMT | Selects depository to be delivered check frequency and call STMT.DELIVERY | SC.BATCH.REP | FIN |
| 146 | SC.STOCK.CONV.SETTLE.POST | Updates SC.SETTLEMENT thru OFS | SC.BATCH.APP | FIN |
| 147 | SC.STOCK.CONV.SETTLE.POST | Updates SC.SETTLEMENT thru OFS | SC.BATCH.START | FIN |
| 148 | SC.STOCK.CONV.SETTLE.POST | Update SC.SETTLEMENT thru OFS | SC.CORPORATE.ACTIONS | FIN |
| 149 | AM.SC.MOVEMENT.ROUNDING | It is one of the job in AM.SC.MOVEMENT batch which round the nominal from each OBC record by reading the record from FBNK.AM.SC.MOVEMENT.ROUNDING work file and update it in FBNK.SC.OBC.CUST.DETAIL file. It also delete the record from FBNK.AM.SC.MOVEMENT.ROUNDING work file after the process gets completed | AM.SC.MOVEMENT | FIN |
| 150 | SC.SOD.ENT.AUTH | Authorises Entitlements records authorize Entitlements records depending the date parameters entered in DIARY.TYPE. | SC.ONLINE | FIN |
| 151 | SC.TRAIL.FEES.BACKUP.EXTRACT | Writes the Extract record with new key concatenated with Payment date | SC.EOD.TRAIL.FEES | CUS |
| 152 | SC.SOD.DIA.AUTH | Authorises diary records that have DIA.AUTO.AUTH.DATE field set to today. | SC.ONLINE | FIN |
| 153 | SC.PL.ADJUST.ACCT | The accounting entries are generated for P/L adjustments. The P/L adjustments are in POS.ADJUSTMENT file | SC.BATCH.APP | FIN |
| 154 | SC.EOD.UPD.DP.SETT.DATE | Dependent routine which is run after the completion of SC.EOD.UPD.SETT.DATE | SC.BATCH.APP | FIN |
| 155 | SC.MT536.UPD.HIS | Moves the trans details to archive file of MT536 outbound message | SC.BATCH.STMT | FIN |
| 156 | EOD.CFT.MKT.UPD | Updates SC.CASH.FLOW.TRANS for SECURITY.TRANSFER or POSITION.TRANSFER | SC.BATCH.PERF | FIN |
| 157 | SC.CPMF.ADC.SINGLE.CALC | Calculates Advisory charges on Grouped portfolios with charge type as SINGLE. | SC.SYS.END.OF.DAY | FIN |
| 158 | SC.UPD.TRAIL.FEES.POSTING | Creates a new record in the file SC.TRAIL.FEES.HOLDING | SC.EOD.TRAIL.FEES | CUS |
| 159 | SC.TRAIL.FEES.ACCRUAL.UPDATE | Posts the trailer fee accrual entries based on the setup in SC.TRAIL.FEES.ARRANGEMENT | SC.EOD.TRAIL.FEES | CUS |
| 160 | COB.SC.GROUP.TRADES.ACCOUNTING | Processes all SC.GROUP.TRADES records with forward accounting | SC.BATCH.START | FIN |
| 161 | SC.EXT.ADV.FEES.ACTIVITY | Performs the updation to SC.ADV.FEES.ACTIVITY which is used to calculate advisory fees. | SC.SYS.END.OF.DAY | FIN |
| 162 | EOD.DIV.AUT.REQ | Generates Diary/ DIV.COUP.DET record automatically based on the setup in SC.PARAMETER and SECURITY.MASTERfile | SC.ONLINE | FIN |
| 163 | SC.SOD.DIARY.ARCH | Subroutine to delete the records in SC.PRE.DIARY$NAU or put the live file in history file if the arch.date is raised | SC.BATCH.SOD.CA | FIN |
| 164 | SC.EOD.UPD.STOCK.POS | Builds SC.STOCK.POSITION during End of Day | SC.BATCH.APP | FIN |
| 165 | VAULT.CONTROL.REMOVE | Moves the VAULT.CONTROL records from live to history and deletes the live record | VAULT.PROCESSING | FIN |
| 166 | SEC.OPEN.ORDER.SERVICE.POST | Create EXE and SEC.TRADE record from SEC.OPEN.ORDER.SERVICE.POST work file | SEC.OPEN.ORDER.SERVICE | FIN |
| 167 | SC.EOD.UPD.SETT.DATE | Updates the NEXT.SETT.DATE and LAST.SETT.DATE fields in SECURITY.POSITION and SC.STOCK.POSITION | SC.BATCH.APP | FIN |
| 168 | BOND.LENT.MASTER.EOD | Updates SECURITY.POSITION for the corresponding record of BOND LENT MASTER | SC.BATCH.START | FIN |
| 169 | SC.EOD.BLK.SEC | This EOD routine selects record from the SECURITY.POSITION file which becomes active on the working day and then updates the block on the SECURITY.POSITION and removes the date from the record | SC.BATCH.SOD.CA | FIN |
| 170 | AM.SC.MOVEMENT | It is one of the job in AM.SC.MOVEMENT batch which calls both this routines(ORDER.BY.CUST.RUN and AM.REBALANCE.RUN) in sequence. | AM.SC.MOVEMENT | FIN |
| 171 | EOD.DIV.WARN.LIST | Job to setup dividend requests for a security which is within the date range specified in SC.PARAMETER | SC.BATCH.REP | FIN |
| 172 | SC.PRICE.MOVE.EXCEPTION | Updates PRICE.MOVEMENT file | SC.BATCH.REP | FIN |
| 173 | SC.GENERATE.MT536 | Generates the MT536 Statement of transaction advice | SC.MT536.DELIVERY | FIN |
| 174 | SC.GENERATE.MT536 | Generates the MT536 Statement of transaction advice | SC.BATCH.STMT | FIN |
| 175 | WRITE.SC.VAL.EXTRACT.POST | It is a multi threaded routine to consolidate all the valuation Id to the respective portfolio | SC.VAL.EXTRACT | FIN |
| 176 | SC.SETTLEMENT.SERVICE | Performs the updates to the broker unsettled fields in the customer Security Positions and Security Trans records | SC.SETTLEMENT.SERVICE | FIN |
| 177 | EOD.AUT.REDEM.REQ | Generates automatic redemption requests for maturity dates falling within the start and end dates | SC.ONLINE | FIN |
| 178 | PURGE.OPEN.ORDER.DETAILS.POST | Removes record from work file that were used to tidy up the SC.SOO.CUST.DETAIL file after the parent SOO was moved to $HIS. | SC.BATCH.APP | FIN |
| 179 | SC.EXT.SAFEKEEP.ACTIVITY | Updates SC.SAFEKEEP.ACTIVITY which is used to calculate safekeeping fees. | SC.SYS.END.OF.DAY | FIN |
| 180 | SC.PARENT.CHILD.EXE | This subroutine executes child records on execution of parent record | SC.PARENT.EXECUTION | FIN |
| 181 | SC.SETTLEMENT.SERVICE.POST | End of sc.settlement processing service delete all the records from the processing file | SC.SETTLEMENT.SERVICE | FIN |
| 182 | SC.BULK.CHILD.UPDATE | Updates Certain fields from parent order/trade to child order/trade. | SC.PARENT.CHILD.PROCESSING | FIN |
| 183 | SC.CPMF.SKF.PRATA.CALC | Calculates Safekeeping fees on Grouped portfolios with charge type as PRORATA. | SC.SYS.END.OF.DAY | FIN |
| 184 | SC.UPDATE.TRN.CON.DATE | Updates TRN.CON.DATE from TRN.CON.DATE.TODAY if LOCAL.TRADING in SC.PARAMETER is set | SC.BATCH.APP | FIN |
| 185 | SC.EOD.BULK.PROCESS | END OF DAY BULK PROCESSING | SC.BULK.TRADE | FIN |
| 186 | SC.EOD.BULK.PROCESS | END OF DAY BULK PROCESSING | SC.BATCH.APP | FIN |
| 187 | SR.AUTOMATCH.SERVICE | Matches the records in SR.HOLDINGS | SR.AUTOMATCH.SERVICE | FIN |
| 188 | SC.SOD.ACCR.ACCT | Generates monthly accrual accounting entries | SC.BATCH.START | FIN |
| 189 | SEC.TRADE.SERVICE.POST | Updates details to sec.trade through service | SEC.TRADE.SERVICE | FIN |
| 190 | SC.EOD.POS.ASSET.HIS | Program to copy all transactions of SC.POS.ASSET.WORK to SC.POS.ASSEST.WORK.HIS file. The program SC.EOD.ASSET.WORK.HIS is now obsolete. | SC.SYS.END.OF.DAY | FIN |
| 191 | SC.OFS.BUILD.SEC.TRADE | Generates SEC.TRADE transaction | SC.REINVEST.SERVICE | FIN |
| 192 | SC.OFS.BUILD.SEC.TRADE | Generates SEC.TRADE transaction | SC.ONLINE | FIN |
| 193 | SR.TIDY.MSGS | Subroutine to move ad hoc message data from live to history files | SC.BATCH.RECON | CUS |
| 194 | SC.PORT.CONST.CON.BUILD | Record routine for SC.PORTFOLIO.CONSTRAINT.BUILD | SC.PORT.CONSTRAINT.BUILD | INT |
| 195 | SC.CLEAR.TRANS.REVAL | Clears SC.TRANS.REVAL work file | SC.BATCH.APP | FIN |
| U | EOD.PERFORM.UPDATE | Updates SC.PORT.PERFORM quartely from SC.FUND.FLOW | SC.BATCH.REP | FIN |
| 197 | SP.AGGREGATE.TRADE.AUTHORISE | Authorises the aggregated trade created for consolidated Nostro posting, This should be run only if MT515 is not used to authorise aggregated trade. | SP.AGGREGATE.TRADE.AUTH | FIN |
| 198 | SC.SAFE.FEES.CREATE | Posts fees as a service | SC.SAFE.FEES.POST | FIN |
| 199 | SC.OL.VAL.MASTER | Processes the group and update the position in SC.GROUP.POS.ASSET | SC.GROUP.VALUATION | FIN |
| 200 | SC.OL.VAL.MASTER | Processes the group and update the position in SC.GROUP.POS.ASSET | SC.SYS.END.OF.DAY | FIN |
| 201 | SC.TRAIL.FEES.UPD.BV.EXTRACT | Updates the Extract record with BV.NO.NOMINAL and BV.V.DATE.NOMINAL | SC.TRAIL.FEES.BV.UPDATE | CUS |
| 202 | SC.TRAIL.FEES.UPD.BV.EXTRACT | Updates the Extract record with BV.NO.NOMINAL and BV.V.DATE.NOMINAL | SC.SYS.END.OF.DAY | FIN |
| 203 | VAULT.EXPECT.AUTHORISE | Updates VAULT.TODAY | VAULT.PROCESSING | FIN |
| 204 | SC.TRANS.REVAL.PROCESSING | Revaluates at transaction level | SC.BATCH.APP | FIN |
| 205 | SC.SM.INT.RATE.UPD | Updates interest rate in SECURITY.MASTER | SC.BATCH.START | FIN |
| 206 | SC.CONV.ENTL.NAU.ACCTNG | Generates accounting entries for entitlements | SC.CONV.ENTL.NAU.ACCTNG | FIN |
| 207 | SC.SOD.NAU.DIARY.ARCH | Subroutine that deletes the records in SC.PRE.DIARY$NAU or put the live file in history file if the arch.date is raised | SC.BATCH.SOD.CA | FIN |
| 208 | SC.BULK.CHILD.AUTH.POST | Authorises all the parent orders/trades | SC.PARENT.CHILD.PROCESSING | FIN |
| 209 | SC.SETTLE.EOD.HLD | Moves settlement transactions that are considered as free receipts to Hold during COB | SC.BATCH.APP | FIN |
| 210 | EOD.SC.VAL.FREQUENCY | Produces valuation reports based on customer security frequency | SC.BATCH.VAL | FIN |
| 211 | SC.BLD.UPFRONT.POSITION.SERVICE | Creates multiple security transfer records | SC.BLD.UPFRONT.POSITION.SERVICE | FIN |
| 212 | SC.SEC.TIME.SERIES.UPDATE | Updates SC.SEC.TIME.SERIES on a daily basis if MAINT.TIME.SERIES is set in SM.PARAMETER | SC.CLEAR.CASHFLOW | FIN |
| 213 | SC.OVER.SUBSCRIPTION.SERVICE | Over subscription Service | SC.OVER.SUBSCRIPTION.SERVICE | FIN |
| 214 | SC.UPD.RECALC.FEES.ARRANGEMENT | Recalculates the extracts with average price provided by issuer | SC.RECALC.TRAIL.FEES | CUS |
| 215 | SC.UPD.RECALC.FEES.HOLDING | Updates Recalculated fees by average price in Holding | SC.RECALC.TRAIL.FEES | CUS |
| 216 | SC.ONLINE.SETT.DATE.ACCTG | This is the record routine for the batch job SC.ONLINE.SETT.DATE.ACCTG | SC.ONLINE.SETT.DATE.ACCTG | FIN |
| 217 | SC.SWITCH.TRANSMISSION |  | SC.GRP.ORD.SERVICE | FIN |
| 218 | SC.GEN.PRE.DIARY.ADV | - This is the record routine for the batch job SC.GEN.PRE.DIARY.ADV. - This routine generates the notification/advice using details from SC.PRE.DIARY - Records and updates the ENTITLEMENT.PRE.DIARY file with the details of   notification message sent. | SC.GEN.PRE.DIARY.ADV | FIN |
| 219 | SR.EOD.RECON | Subroutine to automatically send a SWIFT MT570 (MT549) requesting an MT571 (MT535) for all DEPOSITORIES due to be reconciled. Run as part of the End of Day batch. | SC.BATCH.RECON | CUS |
| 220 | SC.IPO.ORDER.ACCTG | Generates entries during COB | SC.BATCH.APP | FIN |
| 221 | SC.SOD.CREATE.CHILD.DIARY | Creates Child diary when Parallel Trading is set | SC.ONLINE | FIN |
| 222 | SC.SOD.MT565.GEN | Generates MT565 automatically when MT565.AUT.DATE is set Today | SC.ONLINE | FIN |
| 223 | SC.SOD.PRE.DIA.AUTH | Authorises Pre Diary records that have AUTO.AUTH.DATE field set to today. | SC.ONLINE | FIN |
| 224 | SC.UPD.ENT.NOMINAL | Updates Prorated Nominal in Entitlement records | SC.PRORATE.ENT.NOMINAL | FIN |
| 225 | SC.UPD.ENT.NOMINAL.POST | Updates Difference quantity in Diary and create SC.ENT.AUTHORISE | SC.PRORATE.ENT.NOMINAL | FIN |
| 226 | SC.PE.POST.MGMT.FEES | Creates the management fees record based on the frequency specified in PE.PRODUCT.EVENTS | SC.SYS.END.OF.DAY | FIN |
| 227 | SC.PE.POST.MGMT.FEES.POST | Post routine for the job SC.PE.POST.MGMT.FEES | SC.SYS.END.OF.DAY | FIN |
| 228 | PE.UPDATE.MGMT.FEES | Updates PE.MANAGEMENT.FEES as COMPLETE | PE.UPDATE.MGMT.FEES | FIN |
| 229 | SC.EOD.BUILD.CG.PORTFOLIO | Builds CG.PORTFOLIO | SC.BATCH.APP | FIN |
| 230 | SC.RECALC.EXCH.CG.PORTFOLIO | Updates the CG.PORTFOLIO based on the Exchange Rate given for the corresponding Period End | SC.RECALC.EXCH.CG.PORT | FIN |
| 231 | SC.UPDATE.CPL.STATUS | Updates the Status and number of records selected in CG.PORTFOLIO.CALC after recalculation | SC.RECALC.EXCH.CG.PORT | FIN |
| 232 | DX.ARCHIVAL.SERVICE | Archival of DX transaction | DX.ARCHIVAL.SERVICE | FIN |
| 233 | SY.ARCHIVAL.SERVICE | Archival of SY transactions | SY.ARCHIVAL.SERVICE | FIN |
| 234 | SC.BUILD.CG.TXN.ENHLIFO | Updates the CG.TXN.BASE.ENHLIFO after the Dividend event | SC.BUILD.CG.TXN.ENHLIFO | FIN |
| 235 | SC.BUILD.CG.TXN.LIFO | Builds the CgTxnBaseLifo table | SC.BUILD.CG.TXN.LIFO | FIN |
| 236 | SC.UPD.FC.CG.PORTFOLIO | Updates Franking Credits in CG.PORTFOLIO | CG.PORTFOLIO.BUILD | FIN |
| 237 | SC.UPD.FC.CG.PORTFOLIO | Updates Franking Credits in CG.PORTFOLIO | SC.BATCH.APP | FIN |
| 238 | SC.UPD.SALE.TXN.ENHLIFO | This is a Multithreaded job that runs as Temenos Transact service to rebuild CG.TXN.BASE.ENHLIFO record based on the sale transaction involved for each CG.TXN.BASE. | SC.UPD.SALE.TXN.ENHLIFO | FIN |
| 239 | SC.UPD.SALE.TXN.ENHLIFO.POST | Delete all the contents from the workfile after processing of CG.TXN.BASE.ENLIFO | SC.UPD.SALE.TXN.ENHLIFO | FIN |
| 240 | CG.FETCH.BASE.IDS | Fetch IDs for Reallocate Base | CG.REALLOCATE.TXN.BASE | FIN |
| 241 | CG.REBUILD.TXN.BASE | Rebuild CG.TXN.BASE | CG.REALLOCATE.TXN.BASE | FIN |
| 242 | CG.UPD.REALLOCATE.STATUS | Change the Status to PROCESSED | CG.REALLOCATE.TXN.BASE | FIN |
| 243 | CG.BUILD.CG.PORTFOLIO | Process of building the CG.PORTFOLIO | CG.PORTFOLIO.BUILD | FIN |
| 244 | CG.BUILD.CG.PORTFOLIO.POST | Post processing to identify Session records of CG.PORTFOLIO and rebuilding data | CG.PORTFOLIO.BUILD | FIN |
| 245 | CG.PORT.BUILD.FETCH.BASE.IDS | Fetch IDs for Portfolio Build application | CG.PORTFOLIO.BUILD | FIN |
| 246 | SC.UPD.PORT.DORM.STATUS | Updates dormancy status of portfolio based on dormancy period setup | SC.BATCH.APP | FIN |
| 247 | SC.CHK.CTDY.CA.ADVICE | This routine gets the entitlement ids for the pre diary or diary record and check whether to generate the message against SC.CTDY.CA.ADVICE application | SC.GEN.CTDY.DELIVERY | FIN |
| 248 | SC.UPD.CTDY.CORP.ACTION | This routine simulates the entitlement record to build SC.CTDY.CORP.ACTION and trigger the generation of outward message | SC.GEN.CTDY.DELIVERY | FIN |
| 249 | SC.SOD.MT564.GEN | SC.SOD.MT564.GEN | SC.ONLINE | FIN |
| 250 | SC.BULK.CUSTODIAN.TRANSFER | Creates multiple Position Transfer records based on Bulk Transfer | SC.BULK.TRANSFER.SERVICE | FIN |
| 251 | SC.BULK.TRANSFER.POST | Consolidates the transaction status details in Bulk Transfer | SC.BULK.TRANSFER.SERVICE | FIN |
| 252 | SC.BULK.SETTLEMENT | Performs bulk settlement of Position Transfer generated through SC.BULK.TRANSFER | SC.BULK.POSITION.TRANSFER | FIN |
| 253 | DFE.OUTWARD.FILE.EXTRACT | Generates report based on setup in DFE.PARAMETER and DFE.MAPPING | SCDX.ONLINE.REPORTS | FIN |
| 254 | DFE.OUTWARD.FILE.EXTRACT.POST | Frames the header and trailer details in the report | SCDX.ONLINE.REPORTS | FIN |
| 255 | SC.INC.RECLASSIFICATION | Reclassifies the income defined in diary post the event | SC.INC.RECLASSIFICATION | FIN |
| 256 | SC.INC.RECLASSIFICATION.POST | Deletes the record from income reclassification file once the income classification is processed | SC.INC.RECLASSIFICATION | FIN |

## Structured Products (SY)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | SY.COB.CHECK.PROCESSED | Checks the automatic processing of rolling or scheduled Structured Products Events. This job is common to three phases of the close of business (COB) start of day and online. The DATA field is used to pass in details of which COB phase we are running in: "APPLICATION" "START.OF.DAY" or "ONLINE" respectively. This job is passed the list of SY.EVENT records processed by the previous job SY.COB.PROCESS.EVENTS and reports an error in SY.EVENT.ERRORS if the last run date recorded on the event is less than the system date. | SY.CLOSE.OF.BUSINESS | FIN |
| 2 | SY.COB.CHECK.PROCESSED | Checks the automatic processing of rolling or scheduled Structured Products Events. This job is common to three phases of the COB start of day and online. The DATA field is used to pass in details of which COB phase we are running in: "APPLICATION" "START.OF.DAY" or "ONLINE" respectively. This job is passed the list of SY.EVENT records processed by the previous job SY.COB.PROCESS.EVENTS and reports an error in SY.EVENT.ERRORS if the last run date recorded on the event is less than the system date. | SY.START.OF.DAY | FIN |
| 3 | SY.COB.CHECK.PROCESSED | Checks the automatic processing of rolling or scheduled Structured Products Events. This job is common to three phases of the COB start of day and online. The DATA field is used to pass in details of which COB phase we are running in: "APPLICATION" "START.OF.DAY" or "ONLINE" respectively. This job is passed the list of SY.EVENT records processed by the previous job SY.COB.PROCESS.EVENTS and reports an error in SY.EVENT.ERRORS if the last run date recorded on the event is less than the system date. | SY.ONLINE | FIN |
| 4 | SY.COB.PROCESS.EVENTS | Automatically triggers the processing of rolling or scheduled Structured Products Events. This job is common to three phases of the COB start of day and online. The DATA field is used to pass in details of which COB phase we are running in: "APPLICATION" "START.OF.DAY" or "ONLINE" respectively. Selects all SY.PRODUCT records that are not terminated and then for each product attempts to process each event in turn provided that the event is scheduled or rolling the event is due to run on or before the system date and the COB.PHASE on the event matches the current COB phase. The event is input and authorised with PROCESS flag set if all these conditions are met and the record key is passed to the next job for verification. | SY.CLOSE.OF.BUSINESS | FIN |
| 5 | SY.COB.PROCESS.EVENTS | Automatically triggers the processing of rolling or scheduled Structured Products Events. This job is common to three phases of the COB start of day and online. The DATA field is used to pass in details of which COB phase we are running in: "APPLICATION" "START.OF.DAY" or "ONLINE" respectively. Selects all SY.PRODUCT records that are not terminated and then for each product attempts to process each event in turn provided that the event is scheduled or rolling the event is due to run on or before the system date and the COB.PHASE on the event matches the current COB phase. The event is input and authorised with PROCESS flag set if all these conditions are met and the record key is passed to the next job for verification. | SY.START.OF.DAY | FIN |
| 6 | SY.COB.PROCESS.EVENTS | Automatically triggers the processing of rolling or scheduled Structured Products Events. This job is common to three phases of the COB start of day and online. The DATA field is used to pass in details of which COB phase we are running in: "APPLICATION" "START.OF.DAY" or "ONLINE" respectively. Selects all SY.PRODUCT records that are not terminated and then for each product attempts to process each event in turn provided that the event is scheduled or rolling the event is due to run on or before the system date and the COB.PHASE on the event matches the current COB phase. The event is input and authorised with PROCESS flag set if all these conditions are met and the record key is passed to the next job for verification. | SY.ONLINE | FIN |
| 7 | SY.COB.CLEAR.OFSDET | Selects all records in the OFS.REQUEST.DETAIL table. If the OFS.SOURCE record as referenced in SY.PARAMETER has MAINT.MSG.DETS set to 'Y' deletes each OFS.REQUEST.DETAIL record with the prefix as specified in the field DET.PREFIX. | SY.CLOSE.OF.BUSINESS | FIN |
| 8 | SY.MTM.POSTING | - This routine gets the SY.PRODUCT id as incoming argument and finds whether MTM is required,   or not. - If MTM is required then fetch the SYDX.MARKET.VAL key and get the MTM that is Updated in   SYDX.MARKET.VAL record. - Build the accounting entry for the MTM amount by calling SY.MTM.BUILD.ENTRY and then pass   the accounting   array to EB.ACCOUNTING to generate the accounting entries. | SY.MTM.POSTING | FIN |
| 9 | SY.STATIC.CHANGES | CONSOL.KEY.TYPE Static change update for SY applications | SY.CLOSE.OF.BUSINESS | FIN |
| 10 | SY.COB.ACCRUED.INT | Calculates accrued interest based on the transaction attributes | SY.CLOSE.OF.BUSINESS | FIN |

## Teller (TT)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | TELLER.EOD.2 | Moves Teller contracts to history based on AUTH.DATE . Selection file : TELLER | TT.END.OF.DAY | FIN |
| 2 | PB.CONS.STMT.UPDATE |  | TELLER.PASSBOOK.STMT | FIN |
| 3 | TELLER.STMT.UPDATE | Updates ACCOUNT.STATEMENT for passbook accounts based on TELLER.PBOOK.PRINTED update ACCOUNT.STMT and deletes it. Selection file: TELLER.PBOOK.PRINTED | TELLER.PASSBOOK.STMT | FIN |

## Transaction Restriction (TZ)

| S.No | Job Name | Description of Job | Batch name | Classification |
| --- | --- | --- | --- | --- |
| 1 | TZ.STOP.INSTR.AC.TAKEON | Converts Account based Concat file for Stop Instruction into Customer based file | TZ.STOP.INSTR.AC.TAKEON | FIN |
| 2 | TRANS.STOP.ARCHIVE | Moves the Stop Instruction to either EXPIRED status or to History | TRANS.STOP.ARCHIVE | FIN |



In this topic

- [Temenos Transact Services](#TemenosTransactServices)

- [Accounting Unit (AU)](#AccountingUnitAU)
- [Accounts (AC)](#AccountsAC)
- [All in One (AZ)](#AllinOneAZ)
- [Arrangement Architecture (AA)](#ArrangementArchitectureAA)
- [Cheque & Draft Issue Management (CQ)](#ChequeDraftIssueManagementCQ)
- [Centralised Reference Data (RD)](#CentralisedReferenceDataRD)
- [Collateral Management (CO,CX)](#CollateralManagementCOCX)
- [Collections (CL)](#CollectionsCL)
- [Confirmation Matching (CM)](#ConfirmationMatchingCM)
- [Contact Preferences (PF)](#ContactPreferencesPF)
- [Currency Redenomination (EU)](#CurrencyRedenominationEU)
- [Customer & Account Balance Reporting Model (DA)](#CustomerAccountBalanceReportingModelDA)
- [Delivery (DE)](#DeliveryDE)
- [Derivatives (DX)](#DerivativesDX)
- [Digital
  Investments/Dual and Triple Currency Investments (DI)](#DigitalInvestmentsDualandTripleCurrencyInvestmentsDI)
- [Direct Debits (DD)](#DirectDebitsDD)
- [Equity Accumulator (DP)](#EquityAccumulatorDP)
- [European Savings Directive (ET)](#EuropeanSavingsDirectiveET)
- [Fiduciary Deposits (FD)](#FiduciaryDepositsFD)
- [Funds Transfer (FT)](#FundsTransferFT)
- [General Ledger (RE)](#GeneralLedgerRE)
- [Interest & Charges (IC)](#InterestChargesIC)
- [ISO20022 - ACCOUNT REPORTING (IX)](#ISO20022ACCOUNTREPORTINGIX)
- [Limits (LI)](#LimitsLI)
- [Loans and Deposits (LD)](#LoansandDepositsLD)
- [Lombard Lending (OV)](#LombardLendingOV)
- [Nostro Reconcilliation (NR)](#NostroReconcilliationNR)
- [Past Due (PD)](#PastDuePD)
- [Pricing in AA (PR)](#PricinginAAPR)
- [Repurchase Agreements (RP)](#RepurchaseAgreementsRP)
- [Retail Bundle (AB)](#RetailBundleAB)
- [Retail Lending (AL)](#RetailLendingAL)
- [Securities (SC)](#SecuritiesSC)
- [Structured Products (SY)](#StructuredProductsSY)
- [Teller (TT)](#TellerTT)
- [Transaction Restriction (TZ)](#TransactionRestrictionTZ)


Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Thursday, April 16, 2026 11:12:21 PM IST
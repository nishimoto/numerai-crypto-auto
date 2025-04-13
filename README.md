
# 📈 Numerai Crypto Submission Automation via Cloud Run

このリポジトリは、[Numerai Crypto Tournament]([https://numer.ai/crypto](https://crypto.numer.ai/)) におけるモデルの予測ファイルを、Kaggle Kernel からダウンロードして、自動的にアップロードする処理を Google Cloud Run 上で自動化するためのスクリプトを含みます。

## 📦 構成

- Python + Cloud Functions Framework（`functions_framework`）
- Kaggle Kernel から `.csv` をダウンロード
- Numerai Crypto API を用いて複数のモデルに提出
- GCP Cloud Run にデプロイして定期実行可能

## 🧩 事前準備

### 環境変数

 - `KAGGLE_USERNAME`
 - `KAGGLE_KEY`
 - `numerai_public_id`
 - `numerai_secret_key`

これらは Cloud Run の **環境変数** に設定。

## 📝 注意事項

- Kaggle API では Kernel の出力を取得する際に少し時間がかかるため、Cloud Run のタイムアウト設定を長め（300秒など）にしてください。

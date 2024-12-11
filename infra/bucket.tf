terraform {
  required_version = ">= 1.0.0"
  required_providers {
    b2 = {
      source = "Backblaze/b2"
    }
  }
}

provider "b2" {
}


resource "b2_bucket" "research_documents" {
  bucket_name = "research-documents"
  bucket_type = "allPrivate"
}

resource "b2_application_key" "research_docs_read" {
  key_name     = "beam-marker-converter"

  capabilities = [
    "listFiles",
    "readFiles",
    "shareFiles"
  ]
  bucket_id = b2_bucket.research_documents.bucket_id
}

resource "b2_bucket_file_version" "name" {
  bucket_id = b2_bucket.research_documents.bucket_id
  file_name = "demikernel.pdf"
  source = "../ignore/demikernel.pdf"
}
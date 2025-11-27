"""Sample training script demonstrating MLFlow usage patterns."""

import mlflow


def train(learning_rate: float = 0.01, epochs: int = 10) -> dict:
    """Train a model and log metrics to MLFlow.

    Args:
        learning_rate: Learning rate for the optimizer.
        epochs: Number of training epochs.

    Returns:
        Dictionary containing final metrics.
    """
    with mlflow.start_run():
        # Log parameters
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("epochs", epochs)

        # Simulate training loop
        for epoch in range(epochs):
            # Replace with actual training logic
            loss = 1.0 / (epoch + 1) * learning_rate
            accuracy = 1 - loss

            mlflow.log_metrics({"loss": loss, "accuracy": accuracy}, step=epoch)

        # Log final metrics
        final_metrics = {"final_loss": loss, "final_accuracy": accuracy}
        mlflow.log_metrics(final_metrics)

        # Log model artifact (uncomment when you have a real model)
        # mlflow.sklearn.log_model(model, "model")

    return final_metrics


if __name__ == "__main__":
    results = train(learning_rate=0.01, epochs=10)
    print(f"Training complete: {results}")
